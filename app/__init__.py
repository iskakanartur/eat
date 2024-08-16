from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import config

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIG', config_name).lower()
    app.config.from_object(config[config_name])
    app.config.from_envvar('APP_SETTINGS', silent=True)

    db.init_app(app)

    from app import models

    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
