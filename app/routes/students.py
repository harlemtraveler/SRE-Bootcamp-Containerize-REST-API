from flask import Blueprint, request, jsonify
from app.models import Student
from app.db import db

students_bp = Blueprint('students', __name__)

# Query all Students
@students_bp.route('/', methods=['GET'])
def get_students():
    return jsonify([{'id': s.id, 'name': s.name} for s in Student.query.all()])

# Query single Student by ID
@students_bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    s = Student.query.get_or_404(id)
    return jsonify({'id': s.id, 'name': s.name, 'age': s.age, 'grade': s.grade})

# Add Student
@students_bp.route('/', methods=['POST'])
def add_student():
    data = request.get_json()
    s = Student(name=data['name'], age=data['age'], grade=data['grade'])
    db.session.add(s)
    db.session.commit()
    return jsonify({'message': 'Student added'}), 201

# Update single Student by ID
@students_bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    s = Student.query.get_or_404(id)
    s.name = data.get('name', s.name)
    s.age = data.get('age', s.age)
    s.grade = data.get('grade', s.grade)
    db.session.commit()
    return jsonify({'message': 'Student updated'})

# Delete single Student by ID
@students_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    s = Student.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})