import os

class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/desk'
    


class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/desk'

    DEBUG = True


config_options = {
    'developmnet':DevConfig,
    'development':ProdConfig,
    'test':TestConfig
}
