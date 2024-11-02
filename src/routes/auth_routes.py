# backend/routes/auth_routes.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from src.models.user import User
from src import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # Mặc định là "user"

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(username=username, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={"username": user.username, "role": user.role})
        refresh_token = create_refresh_token(identity="username")
        return jsonify(access_token=access_token, refresh_token=refresh_token, username=username, password=password,
                       role=user.role), 200
    return jsonify({"msg": "Invalid credentials"}), 401


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@auth_bp.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"msg": "Admin access required"}), 403
    return jsonify({"msg": "Welcome, admin!"}), 200


# # Refresh Token Route
# @auth_bp.route('/refresh', methods=['POST'])
# def refresh():
#     current_user = get_jwt_identity()
#     new_access_token = create_access_token(identity=current_user)
#     return jsonify(access_token=new_access_token), 200
