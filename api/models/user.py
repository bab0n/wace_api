from .db import db
import jwt
from flask import current_app
from flask_restx import abort


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status = db.Column(db.Text, nullable=True, default='user')
    phone = db.Column(db.Text, nullable=True)
    name = db.Column(
        db.Text, nullable=True, default='Пользователь'
    )  # Представляемое в личном кабинете имя
    balance = db.Column(db.Float, nullable=True, default=0.0)
    tarif = db.Column(db.Text, nullable=True, default=None)  # Название тарифа подписки
    subscribe = db.Column(db.Integer, nullable=True, default=0)  # Кол-во дней подписки
    buyDate = db.Column(db.Text, nullable=True, default=None)  # Дата покупки подписки
    wbkey = db.Column(db.Text, nullable=True, default=None)
    autofeedback = db.Column(
        db.Boolean, nullable=True, default=False
    )  # Включены ли ответы на отзывы
    autoqeusts = db.Column(
        db.Boolean, nullable=True, default=False
    )  # Включены ли ответы на вопросы

    @classmethod
    def getByToken(cls, token):
        key = current_app.config.get("SECRET_KEY")
        try:
            login = jwt.decode(token, key, algorithms=['HS256']).get('login')
            res = cls.query.filter_by(phone=login).first()
            return abort(402, 'User with this token not found') if res is None else res
        except Exception:
            abort(401, 'Token is invalid')
            return None

    def save(self):
        db.session.commit()

    def add_new(self):
        db.session.add(self)
        db.session.commit()
        self.chainCreate()

    def chainCreate(self):
        templates = UserTemplates(self.id)
        templates.addNew()

    def getInfo(self):
        temp = self.__dict__
        del temp['_sa_instance_state']
        return temp


class UserTemplates(db.Model):
    userid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    aiWork = db.Column(db.Boolean, nullable=True, default=False)
    star1 = db.Column(db.Text, nullable=True)
    star2 = db.Column(db.Text, nullable=True)
    star3 = db.Column(db.Text, nullable=True)
    star4 = db.Column(db.Text, nullable=True)
    star5 = db.Column(db.Text, nullable=True)
    feedback = db.Column(db.Text, nullable=True)
    quest = db.Column(db.Text, nullable=True)

    def __init__(self, id):
        self.userid = id

    def addNew(self):
        db.session.add(self)
        db.session.commit()
