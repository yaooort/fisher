"""
    创建日期 2019-01-31 23:22
    创建人   yao 心愿模型类似赠书模型，抽象行为对象
"""

from sqlalchemy import Integer, Column, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db

from app.spider.yushu_book import YuShuBook

__author__ = 'Oort'


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [EachGiftWishCount(w[0], w[1]) for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


from app.models.gift import Gift, EachGiftWishCount
