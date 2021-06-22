from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager= LoginManager()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    '''creating the app configuration'''
    
    # initialising the extensions 
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)



    # registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    
    return app
