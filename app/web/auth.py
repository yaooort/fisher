"""
    创建日期 2019-01-31 16:35
    创建人   yao
"""

from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.libs.email import send_email
from app.models.base import db
from app.models.user import User
from . import web

__author__ = 'Oort'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST' and form.validate():
        account_email = form.email.data
        user = User.query.filter_by(email=account_email).first_or_404()
        send_email(to=account_email, subject="重置您的密码", template="email/reset_password.html", user=user,
                   token=user.generate_token())
        flash("重置密码邮件已发送到您的注册邮箱，请查收！")
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate() and token:
        result, msg = User.reset_password(token, form.password1.data)
        if result:
            flash("密码重置成功")
            return redirect(url_for('web.login'))
        else:
            flash("密码重置失败,失败原因" + msg)

    return render_template('auth/forget_password.html', form=form)


@web.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))
