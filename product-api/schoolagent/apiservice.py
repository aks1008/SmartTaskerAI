from app.models import Student
from flask import jsonify

def get_student_list():
    """
    Fetches the list of students details like name, studentId, totalMarks, emergencyContact, dateOfBirth, className.
    """
    students = Student.query.all()
    print('students:', students)
    return [{'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact} for student in students]