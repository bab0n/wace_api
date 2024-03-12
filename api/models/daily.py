from .db import db


class Daily(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    enable = db.Column(db.Boolean, nullable=True)
    time = db.Column(db.Text, nullable=True)
    orders = db.Column(db.Boolean, nullable=True)
    sales = db.Column(db.Boolean, nullable=True)
    returns = db.Column(db.Boolean, nullable=True)
    cancels = db.Column(db.Boolean, nullable=True)
    penaltys = db.Column(db.Boolean, nullable=True)
    topOrders = db.Column(db.Boolean, nullable=True)
    topBuys = db.Column(db.Boolean, nullable=True)
