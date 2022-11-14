from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'minha_secret_key'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
    'development':DevelopmentConfig,
    'default': DevelopmentConfig
}