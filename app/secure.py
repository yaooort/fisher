"""
Created by Oort on 2018/12/6 3:14 PM.
"""

__author__ = 'Oort'
# 是否调试模式
DEBUG = True
# 秘钥
SECRET_KEY = '\x03HNK\xa5?X\xe8\xe2y\r\xd2\xb9v\xd6F\xce\xa3\xae\xa5\x8b\x12\xbd\xdeP\xfe\xa9\xa0\xea \xf4\xafY6\x94X\xc42\xcc\x97\xd4\x9e\xcc\x1a\xba\xca\xb0\x07'
# 数据库用户名
MYSQL_NAME = 'root'
# 数据库密码 私人电脑 111111 公司 11111111
MYSQL_PASSWORD = '11111111'
# 数据库连接地址
MYSQL_ADDRESS = '127.0.0.1'
# 数据库端口
MYSQL_PORT = '3306'
# 数据库名称
MYSQL_DB_NAME = 'fisher'
# 默认数据库编码方式
MYSQL_CHARSET = 'utf8'
# 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
# SQLALCHEMY_ECHO = True
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 数据库链接
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://' + MYSQL_NAME + ':' + MYSQL_PASSWORD + '@' + MYSQL_ADDRESS + ':' + MYSQL_PORT + '/' + MYSQL_DB_NAME + '?charset=' + MYSQL_CHARSET

# Email配置
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = ('小鱼', 'yaooort@gmail.com')
MAIL_MAX_EMAILS = 10
MAIL_USERNAME = 'yaooort@gmail.com'
MAIL_PASSWORD = 'YaoOort123'
