from flask import Blueprint, request, jsonify
from .models import User, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], preferences=data.get('preferences', {}))
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'User created'}), 201

@user_bp.route('/<user_id>/preferences', methods=['PUT'])
@jwt_required()
def update_preferences(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.preferences = data['preferences']
    db.session.commit()
    return jsonify({'msg': 'Preferences updated'})

@user_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'preferences': user.preferences
    })
