import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', '2020$$$NBLOGSEC')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEF_SENDER = ('NBLOG Admin', MAIL_USERNAME)

    NBLOG_EMAIL = os.getenv('NBLOG_EMAIL')
    NBLOG_POST_PER_PAGE = 10
    NBLOG_MANAGER_POST_PER_PAGE = 15
    NBLOG_COMMENT_PER_PAGE = 15

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URL')

class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('PRO_DB_URL')

config = {
    'development': DevConfig,
    'production': ProConfig,
    'default': DevConfig
}