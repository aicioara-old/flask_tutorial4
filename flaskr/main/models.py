import datetime
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func




# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     password = db.Column(db.String, nullable=False)



# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     author = db.relationship("User", backref=db.backref('posts', lazy=True))
#     created = db.Column(db.DateTime(timezone=False), nullable=False, server_default=func.now())
#     title = db.Column(db.String, nullable=False)
#     body = db.Column(db.String, nullable=False)

