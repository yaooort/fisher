"""
    创建日期 2019-01-31 16:40
    创建人   yao
"""
from . import web

__author__ = 'Oort'


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
