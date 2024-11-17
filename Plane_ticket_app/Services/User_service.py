from flask import Flask,request
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    @staticmethod
    def create_User(self):
        data = request.get_json()
        username = data.get('username')
        name = data.get('name')
        email = data.get('email')
        hashed_password = generate_password_hash(data.get('password'),method='sha256')
        phone_number = data.get('phone_number')

        if not all(username,name,email,hashed_password,phone_number):
            return f'Unable to create user.'
        
        new_user = User(username=username,name=name,email=email,hashed_password=hashed_password,phone_number=phone_number)
        return new_user

    @staticmethod
    def get_user_by_user_id():
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return 'user_id not given.'
        
        user = User.query.filter_by(user_id=user_id)
        return user
    
    @staticmethod
    def verify_user():
        data = request.get_json()
        username = data.get('username')
        password = check_password_hash(data.get('password'),hashed_password)

        

        return 'verified user', 200