from .db import db


class Promocode(db.Model):
    text = db.Column(db.Text, primary_key=True)
    activs = db.Column(db.Integer, nullable=True)
    discount = db.Column(db.Integer, nullable=True)
