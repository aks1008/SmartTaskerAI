from flask import Flask
from app.models import db
from flask_cors import CORS
from app.app_routes.student import student_ns
from app.app_routes.chatbot import chatbot_ns
from flask_restx import Api

app = Flask(__name__)
CORS(app)

# Load config from config.py
app.config.from_object('app.config.Config')

api = Api(app, version='1.0', title='My API', description='Swagger docs')

api.add_namespace(student_ns, path='/api/students')
api.add_namespace(chatbot_ns, path='/api/chatbot')

db.init_app(app)

# Create DB tables
with app.app_context():
    db.create_all()