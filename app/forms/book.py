"""
Created by Oort on 2018/12/6 2:53 PM.
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = 'Oort'


class SearchForm(Form):
    """
    搜索书籍的From 数据监测
    """
    # DataRequired 字段不能为空 Length 长度限制
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='查询关键字长度必须是1~30')])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message='页数超出限制')], default=1)
