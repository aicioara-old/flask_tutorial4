import os
import datetime

import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def init_app(app):
    app.cli.add_command(init_db_command)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_db():
    from . import models
    models.db.create_all()
    user = models.User(username='admin', password=generate_password_hash('admin'))
    models.db.session.add(user)
    models.db.session.commit()


