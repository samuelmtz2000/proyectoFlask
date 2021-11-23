class Config(object):
    SECRET_KEY = "seguridad"
    SESSION_COOKIE_SECURE = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1/proyectoLogin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
