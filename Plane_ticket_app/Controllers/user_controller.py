from flask import render_template,request,redirect,url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import login_required, current_user, login_manager
from Plane_ticket_app.Services.user_service import UserService
from Plane_ticket_app.templates.user_view import UserView

class UserController:
    @staticmethod
    def register():
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return render_template('render.html',"Missing required fields"), 400

        user = UserService.register_user(username, email, password)
        return render_template('user_profile.html'), 201

    @staticmethod
    def login():
        data = request.form
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Missing required fields"}, 400

        response, status_code = UserService.authenticate_user(username, password)

        if status_code == 200:
            if username == 'admin':
                return render_template('admin.html'), 200
            else:
                return render_template('user_profile.html'), 200

        return render_template('render.html',message='Invalid username or Password'), 401


    @staticmethod
    @jwt_required()
    def get_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if not user: 
            return render_template('render.html', message='user not found'), 404
        return UserView.render_user(user), 200

    @staticmethod
    def logout():
        UserService.logout_user()
        return render_template('home.html', message='Logout successful'), 200