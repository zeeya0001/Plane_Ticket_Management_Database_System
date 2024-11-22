from flask import Blueprint
from Plane_ticket_app.Controllers.user_controller import UserController
from Plane_ticket_app.middleware.auth_middleware import admin_required

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

# @user_bp.route('/users', methods=['GET'])
# def get_all_users():
#     return userController.get_all_users()

@user_bp.route('/user_register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        return UserController.register()

@user_bp.route('/user/login', methods=['POST'])
def login():
    return UserController.login()

@user_bp.route('/admin', methods=['GET'])
@admin_required
def admin_dashboard():
    return render_template('admin.html'), 200