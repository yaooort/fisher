"""
    创建日期 2019-01-31 16:53
    创建人   yao
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SmallInteger, Column

__author__ = 'Oort'

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # 让ORM创建数据表时忽略此表
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
