class Config(object):
    SECRET_KEY = 'secret key'
    # SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/qa_db"
    # 建议不要使用root用户，最好一个项目创建一个用户
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://qa:qa@localhost:3306/qa_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    QUESTION_URL = 'https://segmentfault.com/questions/hottest'
    # 设置每次请求结束后会自动提交数据库中的改动
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    # SQLALCHEMY_ECHO = True


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
