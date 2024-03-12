from .db import db


class Tarifs(db.Model):
    title = db.Column(db.Text, primary_key=True)  # Название
    describe = db.Column(db.Text, nullable=True)  # Описание
    access = db.Column(db.Text, nullable=True)  # Описание доступа
    days = db.Column(db.Text, nullable=True)  # кол-во днкй формат 7;30;180
    price = db.Column(db.Text, nullable=True)  # цены формат 150;300;700
    purchases = db.Column(db.Integer, nullable=True)  # Ограничение на кол-во покупок
    accessLevel = db.Column(db.Integer, nullable=True)  # Уровень доступа к функциям

    def getPrices(self) -> list:
        return self.price.split(';')

    def getDays(self) -> list:
        return self.days.split(';')

    def getDaysByPrice(self, price) -> str | None:
        days = self.getDays()
        prices = self.getPrices()
        if price not in prices:
            return None
        else:
            return days[prices.index(price)]
