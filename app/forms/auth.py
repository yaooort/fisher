"""
    创建日期 2019-01-31 17:04
    创建人   yao
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from app.models.user import User

__author__ = 'Oort'


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


class PassWordForm(Form):
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class RegisterForm(PassWordForm, EmailForm):
    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_email(self, field):
        # db.session.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(PassWordForm, EmailForm):
    pass


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32, message="请输入6-32位密码"),
        EqualTo('password2', message="两次输入密码不相同")])
    password2 = PasswordField(DataRequired(message='密码不可以为空，请输入你的密码'))
