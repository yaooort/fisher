from threading import Thread

from app import mail
from flask_mail import Message
from flask import current_app, render_template


def send_sync_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    """
    发送电子邮件
    :return:
    """
    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    Thread(target=send_sync_email, args=[app, msg]).start()
