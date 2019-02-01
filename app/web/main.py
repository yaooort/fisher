"""
    创建日期 2019-01-31 16:41
    创建人   yao
"""
from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web

__author__ = 'Oort'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
