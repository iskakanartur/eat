from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Food
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/add', methods=['GET', 'POST'])
@bp.route('/add/<int:food_id>', methods=['GET', 'POST'])
def add_food(food_id=None):
    if request.method == 'POST':
        if food_id:
            food = Food.query.get_or_404(food_id)
            food.date = datetime.now()
            food.dish = request.form['dish']
            food.ingredients = request.form['ingredients']
            food.grams = float(request.form['grams'])
            food.calories = float(request.form['calories'])
            food.meal = request.form['meal']
            food.portion = float(request.form['portion'])

            food.calculate_dish_calories()
            food.calculate_portion_calories()
            food.calculate_daily_calories()
        else:
            dish = request.form['dish']
            ingredients = request.form['ingredients']
            grams = float(request.form['grams'])
            calories = float(request.form['calories'])
            meal = request.form['meal']
            portion = float(request.form['portion'])

            portion_calories = (calories * portion) / 100

            today = datetime.now().date()
            daily_calories_query = db.session.query(db.func.sum(Food.portion_calories)).filter(Food.date == today)
            daily_calories = daily_calories_query.scalar()
            daily_calories = daily_calories if daily_calories is not None else 0
            daily_calories_consumed = daily_calories + portion_calories

            new_food = Food(
                date=datetime.now(),
                dish=dish,
                ingredients=ingredients,
                grams=grams,
                calories=calories,
                dish_calories=None,
                meal=meal,
                portion=portion,
                portion_calories=portion_calories,
                daily_calories_consumed=daily_calories_consumed
            )

            db.session.add(new_food)

        db.session.commit()

        return redirect(url_for('main.index'))

    food = Food.query.get(food_id) if food_id else None
    return render_template('add_food.html', food=food)

@bp.route('/delete/<int:food_id>', methods=['POST'])
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return redirect(url_for('main.view_food'))

@bp.route('/view')
def view_food():
    foods = Food.query.all()
    return render_template('view_food.html', foods=foods)
