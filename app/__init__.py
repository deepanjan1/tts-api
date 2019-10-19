from flask import Flask, request, current_app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

# import slack
import os

# local imports
from config import (
    config_options,
    DevelopmentConfig,
    # ProductionConfig,
    TestingConfig,
)

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
admin = Admin(name='mycast', template_mode='bootstrap3')


def create_app(config_name):
    app = Flask(__name__)
    # temporary fix
    # if config_name == 'production':
    #     app.config.from_object(ProductionConfig)
    if config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # initialize flask extensions
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    # set logging
    app.logger.setLevel(logging.INFO)
    app.logger.info('mycast logging')
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", default=False)

    # register blueprints
    # tracks
    from app.tracks import bp as tracks_bp
    app.register_blueprint(tracks_bp, url_prefix='/tracks')

    # # bot
    # from app.bot import bp as bot_bp
    # app.register_blueprint(bot_bp, url_prefix='/bot')

    # # admin
    # from app.admin import bp as admin_bp
    # app.register_blueprint(admin_bp, url_prefix='/admin')

    # # checkup
    # from app.checkup import bp as checkup_bp
    # app.register_blueprint(checkup_bp, url_prefix='/checkup')

    return app

from app import models
