from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
from app.models import Student, db

student_bp = Blueprint('student', __name__)
CORS(student_bp)

# CREATE a new student
@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('dateOfBirth'):
        abort(400, 'Name and date of birth are required.')
    className = data.get('className', '')
    totalMarks = data.get('totalMarks', 0)
    emergencyContact = data.get('emergencyContact', '')
    student = Student(name=data['name'], dateOfBirth=data['dateOfBirth'], className=className, totalMarks=totalMarks, emergencyContact=emergencyContact)
    db.session.add(student)
    db.session.commit()
    return jsonify({'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact}), 201

# READ all students
@student_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([
        {'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact}
        for student in students
    ])

# READ a single student by id
@student_bp.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify({'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact})

# UPDATE a student by id
@student_bp.route('/students/<string:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    student.name = data.get('name', student.name)
    student.dateOfBirth = data.get('dateOfBirth', student.dateOfBirth)
    student.className = data.get('className', student.className)
    student.totalMarks = data.get('totalMarks', student.totalMarks)
    student.emergencyContact = data.get('emergencyContact', student.emergencyContact)
    db.session.commit()
    return jsonify({'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact})

# DELETE a student by id
@student_bp.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': f'Student {student_id} deleted'})
