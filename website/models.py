from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(30))
    pages = db.relationship("Pages")

class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # use foreign key to link topics to pages

class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))

#class SiteTopics(db.Model):
#   id = db.Column(db.Integer, primary_key=True)