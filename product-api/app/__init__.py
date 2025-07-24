from flask import Flask
from app.models import db
from app.routes import register_blueprints

app = Flask(__name__)

# Load config from config.py
app.config.from_object('app.config.Config')

db.init_app(app)

register_blueprints(app)

# Create DB tables
with app.app_context():
    db.create_all()