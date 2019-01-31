"""
    创建日期 2019-01-31 17:09
    创建人   yao
"""
from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = 'Oort'


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
