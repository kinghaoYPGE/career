class Config(object):
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/qa_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    QUESTION_URL = 'https://segmentfault.com/questions/hottest'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
