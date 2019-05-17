from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name


db = SQLAlchemy()


def create_app(config_name='dev'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app
