"""
    创建日期 2019-01-31 16:41
    创建人   yao
"""
from . import web

__author__ = 'Oort'


@web.route('/')
def index():
    pass


@web.route('/personal')
def personal_center():
    pass
