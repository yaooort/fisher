"""
    创建日期 2019-01-31 16:59
    创建人   yao
"""
from math import floor

from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from app import login_manager
from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

__author__ = 'Oort'


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_send_drift(self):
        if self.beans < 1:
            return False
        success_gifts_count = Gift.query.filter_by(uid=self.id, launched=True).count()
        success_receive_count = Drift.query.filter_by(requester_id=self.id, _pending=PendingStatus.Success).count()

        return True if floor(success_receive_count / 2) <= floor(success_gifts_count) else False

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许用户同时赠多本图书，用户既是赠送者，又是索要者
        # 赠书既不在赠书清单，也不在心愿清单
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

    def generate_token(self, expiration=600):
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return serializer.dumps({'id': self.id})

    @staticmethod
    def reset_password(token, raw):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            dict = serializer.loads(token)
        except BadSignature as e:
            return False, e.message
        user_id = dict['id']
        result = False
        with db.auto_commit():
            user = User.query.get(user_id)
            if user:
                user.password = raw
                result = True
        return result, ''

    @property
    def summary(self):
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter) + '/' + str(self.receive_counter)

        )


@login_manager.user_loader
def get_user(uid):
    return User.query.get(uid)
