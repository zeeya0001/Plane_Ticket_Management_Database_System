from flask import Flask,jsonify,request
from flask_jwt_extended import JWTManager,verify_jwt_in_request,get_jwt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)