"""
    创建日期 2019-01-31 23:22
    创建人   yao 心愿模型类似赠书模型，抽象行为对象
"""

from sqlalchemy import Integer, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = 'Oort'


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
