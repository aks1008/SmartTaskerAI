from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    studentId = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dateOfBirth = db.Column(db.String(100), nullable=False)
    className = db.Column(db.String(100), nullable=False)
    totalMarks = db.Column(db.Integer, nullable=False)
    emergencyContact = db.Column(db.String(100), nullable=False)
