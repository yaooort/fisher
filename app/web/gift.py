"""
    创建日期 2019-01-31 16:40
    创建人   yao
"""
from flask import current_app, flash
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from . import web

__author__ = 'Oort'


@web.route('/my/gifts')
@login_required
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务，回滚
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经存在您的赠书清单或者心愿清单，您不能重复添加')


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
