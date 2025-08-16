from flask import request, abort
from app.models import Student, db
from flask_restx import Namespace, Resource

student_ns = Namespace('students', description='Student related operations')

@student_ns.route('/')
class StudentListResource(Resource):
    def post(self):
        """
        Create new student 
        """
        data = request.get_json()
        if not data or not data.get('name') or not data.get('dateOfBirth'):
            abort(400, 'Name and date of birth are required.')
        className = data.get('className', '')
        totalMarks = data.get('totalMarks', 0)
        emergencyContact = data.get('emergencyContact', '')
        student = Student(name=data['name'], dateOfBirth=data['dateOfBirth'], className=className, totalMarks=totalMarks, emergencyContact=emergencyContact)
        db.session.add(student)
        db.session.commit()
        return {'studentId': student.studentId}, 201
    
@student_ns.route('/')
class StudentListResource(Resource):
    def get(self):
        """
        Get list of all students
        """
        students = Student.query.all()
        return [{'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact} for student in students], 200
    
