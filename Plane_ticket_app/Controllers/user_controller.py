from flask import render_template,request,redirect,url_for
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
            return UserView.render_error("Missing required fields"), 400

        user = UserService.register_user(username, email, password)
        return UserView.render_success('user created successfully'), 201

    @staticmethod
    def login():
        data = request.form
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Missing required fields"}, 400

        response, status_code = UserService.authenticate_user(username, password)

        if status_code == 200:
            if response.get('role') == 'admin':
                return render_template('admin.html'), 200
            else:
                return render_template('user_profile.html'), 200

        return UserView.render_error('Invalid Email or Password'), 401


    @staticmethod
    def get_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if not user: 
            return UserView.render_error('user not found'), 404
        return UserView.render_user(user), 200
