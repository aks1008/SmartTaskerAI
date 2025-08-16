from app.models import Student
from flask import jsonify

def get_student_list():
    """
    Fetches the list of students.
    """
    students = Student.query.all()
    return jsonify([
        {'studentId': student.studentId, 'name': student.name, 'dateOfBirth': student.dateOfBirth, 'className': student.className, 'totalMarks': student.totalMarks, 'emergencyContact': student.emergencyContact}
        for student in students
    ])