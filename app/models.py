from app import db
from datetime import datetime

class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    dish = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    grams = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    dish_calories = db.Column(db.Float, nullable=False)
    meal = db.Column(db.String(100), nullable=False)
    portion = db.Column(db.Float, nullable=False)
    portion_calories = db.Column(db.Float, nullable=False)
    daily_calories_consumed = db.Column(db.Float, nullable=False)

    def calculate_dish_calories(self):
        self.dish_calories = self.calories

    def calculate_portion_calories(self):
        self.portion_calories = self.dish_calories * (self.portion / 100)

    def calculate_daily_calories(self):
        total_daily_calories = db.session.query(db.func.sum(Food.portion_calories)).filter(
            Food.date == self.date
        ).scalar() or 0
        self.daily_calories_consumed = total_daily_calories + self.portion_calories

    def __repr__(self):
        return f'<Food {self.dish}>'
