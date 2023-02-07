from app import db
from datetime import datetime


class Application(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(12), index=True, unique=True)
    body = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.utcnow)
