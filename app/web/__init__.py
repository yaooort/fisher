"""
Created by Oort on 2018/12/6 3:03 PM.
"""
from flask import Blueprint
from flask import render_template

__author__ = 'Oort'

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def server_error(e):
    # AOP 思想
    return render_template('500.html'), 500


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
