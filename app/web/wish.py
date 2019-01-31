"""
    创建日期 2019-01-31 16:42
    创建人   yao
"""
from app.web import web

__author__ = 'Oort'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass
