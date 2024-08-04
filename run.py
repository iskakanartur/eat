from app import create_app, db
from flask_migrate import Migrate
import os

config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)

# Initialize Flask-Migrate for handling database migrations
migrate = Migrate(app, db)

# Entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
