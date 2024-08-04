from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object('config.' + config_name.capitalize() + 'Config')
    app.config.from_object('config.Config')
    app.config.from_envvar('APP_SETTINGS', silent=True)

    db.init_app(app)

    from app import models

    # Register the blueprint
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
