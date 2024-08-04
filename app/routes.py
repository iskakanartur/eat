from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Food

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/add', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        # Get form data
        dish = request.form.get('dish')
        ingredients = request.form.get('ingredients')
        grams = request.form.get('grams')
        calories = request.form.get('calories')
        meal = request.form.get('meal')
        portion = request.form.get('portion')
        portion_calories = request.form.get('portion_calories')

        # Create a new Food instance
        new_food = Food(
            dish=dish,
            ingredients=ingredients,
            grams=float(grams),
            calories=float(calories),
            meal=meal,
            portion=float(portion),
            portion_calories=float(portion_calories)
        )

        # Calculate dish and daily calories before committing
        new_food.calculate_dish_calories()
        new_food.calculate_portion_calories()
        new_food.calculate_daily_calories()

        # Add to database
        db.session.add(new_food)
        db.session.commit()

        # Flash a success message
        flash('Food entry added successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('add_food.html')

@bp.route('/view')
def view_food():
    foods = Food.query.all()
    return render_template('view_food.html', foods=foods)
