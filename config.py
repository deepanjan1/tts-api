import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    LANGUAGES = ['en', 'es']
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = os.getenv('SECRET_KEY')

    # @staticmethod
    # def init_app(app):
    #     pass


class DevelopmentConfig(Config):
    DEBUG = True

    # @staticmethod
    # def init_app(app):
    #     pass


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = need testing db
    # WTF_CSRF_ENABLED = False


# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgres://rilrvzqsfmbmaw:debc9d1cc1ca43780a1f99172f86b93c5384eea719f773fae03da4420780b1d8@ec2-23-21-160-38.compute-1.amazonaws.com:5432/d23ap8pdssuk9n'

#     @classmethod
#     def init_app(cls, app):
#         Config.init_app(app)


# class HerokuConfig(ProductionConfig):
#     # SSL_REDIRECT = True if os.environ.get('DYNO') else False

#     @classmethod
#     def init_app(cls, app):
#         ProductionConfig.init_app(app)


config_options = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    # 'production': ProductionConfig,
    # 'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
