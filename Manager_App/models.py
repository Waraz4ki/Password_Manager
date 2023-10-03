from . import db
from sqlalchemy.sql import func

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    notes = db.Column(db.String(1500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Group(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    group_name = db.Column(db.String(), unique = True)
    entrys = db.relationship("Entry")