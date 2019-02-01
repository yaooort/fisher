"""
    创建日期 2019-01-31 16:42
    创建人   yao
"""
from flask import flash, redirect, url_for

from app.models.base import db
from app.models.wish import Wish
from app.web import web
from flask_login import login_required,current_user

__author__ = 'Oort'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已经存在您的赠书清单或者心愿清单，您不能重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))
