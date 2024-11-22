from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


class UserView:
    @staticmethod
    def render_user(user):
        return {
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at.isoformat()
        }


    @staticmethod
    def render_users(users):
        return [ UserView.render_user(user) for user in users]

    @staticmethod
    @jwt_required()
    def get_user():
        from Plane_ticket_app.Controllers.user_controller import UserController
        current_user = get_jwt_identity()
        user_id = current_user.get("id")
        response, status_code = UserController.get_user(user_id)
        return jsonify(response), status_code

    
    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, access_token=None, user_id=None):
        response = {"message": message}
        if access_token:
            response["access_token"] = access_token
        if user_id:
            response["user_id"] = user_id
        return response