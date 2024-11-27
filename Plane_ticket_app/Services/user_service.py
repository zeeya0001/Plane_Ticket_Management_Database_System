from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from shared.models.user_model import User
from shared.utils.db_utils import db
from shared.utils.auth_utils import create_access_token
from flask_jwt_extended import create_access_token, unset_jwt_cookies

class UserService:
    @staticmethod
    def register_user(username, email, password):
        if User.query.filter_by(email=email).first():
            return {"error": "Email already exists"}, 400

        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {username} registered successfully"}, 201

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return {"error": "Invalid credentials"}, 401

        token = create_access_token(identity={"user_id": user.user_id, "role": user.role})
        return {"access_token": token}, 200

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(user_id = user_id).first()
        if user:
            return {"username": user.username, "email": user.email, "role": user.role}, 200
        return {"error": "User not found"}, 404
       
    
    @staticmethod
    def logout_user():
        response = jsonify({"message": "Logout successful"})
        unset_jwt_cookies(response)
        return response, 200
