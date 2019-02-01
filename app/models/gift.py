"""
    创建日期 2019-01-31 17:09
    创建人   yao
"""
from flask import current_app
from sqlalchemy import Integer, Column, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

__author__ = 'Oort'


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(func(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1
        ).group_by(Wish.isbn).all()
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
