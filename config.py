import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')  # Fallback secret key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # Expecting DATABASE_URL in .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass  # Placeholder for any initialization code if needed

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://user@localhost/foo')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')  # Example for dev DB

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

# Example to facilitate importing these classes in your app
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
