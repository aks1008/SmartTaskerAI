from flask import Blueprint, request, jsonify, abort
from app.models import db, User

user_bp = Blueprint('user', __name__)

# CREATE a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        abort(400, 'Name and email are required.')
    balance = data.get('balance', 0.0)
    user = User(name=data['name'], email=data['email'], balance=balance)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'balance': user.balance}), 201

# READ all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {'id': user.id, 'name': user.name, 'email': user.email, 'balance': user.balance}
        for user in users
    ])

# READ a single user by id
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'balance': user.balance})

# UPDATE a user by id
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    if 'balance' in data:
        user.balance = data['balance']
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'balance': user.balance})

# DELETE a user by id
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {user_id} deleted'})
