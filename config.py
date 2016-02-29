# vi $VIRTUAL_ENV/bin/postactivate
#   cd ~/Projects/nyuportal
#   export APP_SETTINGS="config.DevelopmentConfig"
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'nyu_secret_key'

    DATABASE = 'nyues.db'
    DATABASE_PATH = os.path.join(_basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
