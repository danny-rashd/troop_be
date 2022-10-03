from urllib.parse import quote


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret'
    # DATABASE_URI = 'sqlite://:memory:'
    # SQLALCHEMY_DATABASE_URI ='sqlite:///test.db'
    UPLOAD_FOLDER = 'static/uploads'  # changed to relative path
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '465'
    MAIL_USERNAME = 'abc@gmail.com'
    MAIL_PASSWORD = '1234'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True



class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/troop'


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/proj_test'
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/troop'


config_setting = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
