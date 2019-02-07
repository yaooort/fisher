"""
Created by Oort on 2018/12/6 2:53 PM.
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp

__author__ = 'Oort'


class SearchForm(Form):
    """
    搜索书籍的From 数据监测
    """
    # DataRequired 字段不能为空 Length 长度限制
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='查询关键字长度必须是1~30')])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message='页数超出限制')], default=1)


class DriftForm(Form):
    recipient_name = StringField('收件人姓名',
                                 validators=[DataRequired(), Length(min=2, max=20, message="收件人姓名长度必须是2~20个字")])
    mobile = StringField('手机号', validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField('留言')
    address = StringField('邮寄地址', validators=[DataRequired(), Length(min=10, max=70, message='地址还不到10个子，请尽量填写详细地址')])
