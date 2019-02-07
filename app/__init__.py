"""
Created by Oort on 2018/12/6 2:46 PM.
"""

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.models.base import db

__author__ = 'Oort'
login_manager = LoginManager()

mail = Mail()


def create_app():
    """
    创建全局app
    :return: app
    """
    app = Flask(__name__)
    # 加载私有配置
    app.config.from_object('app.secure')
    # 加载公共配置
    app.config.from_object('app.setting')
    # 注册蓝图
    register_blueprints(app)

    # 初始化db
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'  # 未登录时跳转的页面
    login_manager.login_message = '请先登录或注册'  # 设置未登录时给出的提示flash

    mail.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprints(app):
    from app.web.book import web
    app.register_blueprint(web)
