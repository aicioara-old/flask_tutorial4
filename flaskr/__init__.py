import os
import datetime

import click
from flask import Flask
from flask import current_app, g

from flask_restplus import Api, Resource


api = Api()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'flaskr2.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

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
