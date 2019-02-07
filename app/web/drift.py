"""
    创建日期 2019-01-31 16:38
    创建人   yao
"""
from _curses import flash

from flask import url_for, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import desc, or_
from werkzeug.utils import redirect

from app.forms.book import DriftForm
from app.libs.email import send_email
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.book import BookViewModel
from app.view_models.drift import DriftCollection
from . import web

__author__ = 'Oort'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    """
    交易
    :param gid:
    :return:
    """
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_you_self_gift(current_user.id):
        flash("这本书是你自己的，你不能索要自己的书籍")
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)

    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_drift(drift_form=form, current_gift=current_gift)
        send_email(current_gift.user.email, '有人想要一本书', 'email/get_gift.html', wisher=current_user, gift=current_gift)
        return redirect(url_for('web.pending'))
    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter, user_beans=current_user.beans, form=form)


@web.route('/pending')
@login_required
def pending():
    drifts = Drift.query.filter(
        or_(
            Drift.requester_id == current_user.id,
            Drift.gifter_id == current_user.id)
    ).order_by(
        desc(Drift.create_time)).all()
    drift_collection = DriftCollection(drifts, current_user.id)
    return render_template('pending.html', drifts=drift_collection.data)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    with db.auto_commit():
        drift = Drift()
        drift_form.populate_obj(drift)

        drift.gift_id = current_gift.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        drift.gifter_nickname = current_gift.user.nickname
        drift.gifter_id = current_gift.user.id

        book = BookViewModel(current_gift.book)
        drift.book_author = book.author
        drift.book_title = book.title
        drift.book_img = book.image
        drift.isbn = book.isbn
        current_user.beans -= 1
        db.session.add(drift)
