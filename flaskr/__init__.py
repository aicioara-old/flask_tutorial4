import os
import datetime

import click
from flask import Flask
from flask import current_app, g
from flask_restplus import Api, Resource

from .config import config_by_name

api = Api()


def create_app(config_name='dev'):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_by_name[config_name])

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr import commands
    commands.init_app(app)

    from .models import db
    db.init_app(app)

    from .views import auth
    app.register_blueprint(auth.bp)

    # from .views import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')


    api.init_app(app)

    @api.route('/language')
    class Language(Resource):
        def get(self):
            return {
                'hello': 'world',
            }

        def post(self):
            pass

    return app
