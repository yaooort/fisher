"""
    创建日期 2019-01-31 16:42
    创建人   yao
"""
from flask import flash, redirect, url_for, render_template

from app.libs.email import send_email
from app.models.base import db
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.wish import MyWishs
from app.web import web
from flask_login import login_required, current_user

__author__ = 'Oort'


@web.route('/my/wish')
@login_required
def my_wish():
    wishes_of_mine = Wish.get_user_wishes(current_user.id)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_model = MyWishs(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.trades)


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


@web.route('/wish/book/redraw/<isbn>')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('您还没有上传此书，请先点击加入赠书清单')
    else:
        send_email(wish.user.email, '有人想送你一本书', 'email/satisify_wish.html', wish=wish, gift=gift)
        flash('已向他/她发送了一封邮件')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))
