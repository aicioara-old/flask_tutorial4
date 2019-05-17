from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

from .config import config_by_name


db = SQLAlchemy()


def create_app(config_name='dev'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    from .blueprint import bp
    app.register_blueprint(bp)

    return app
