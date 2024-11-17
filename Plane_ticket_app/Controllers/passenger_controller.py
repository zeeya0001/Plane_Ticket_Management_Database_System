from flask import request,render_template,redirect,url_for
from Plane_ticket_app.Services.passenger_services import PassengerService
from Plane_ticket_app.templates.passenger_views import PassengerView

class PassengerController:
    @staticmethod
    def get_passenger(Passenger_ID):
        passenger = PassengerService.get_passenger_by_Passenger_ID(Passenger_ID)
        if not passenger: 
            return PassengerView.render_error('passenger not found'), 404
        return PassengerView.render_passenger(passenger), 200

    @staticmethod
    def create_passenger():
        data = request.form
        Email = data.get('Email')
        password = data.get('password')
        First_name = data.get('First_name', '')
        Last_name = data.get('Last_name', '')
        Passport_number = data.get('Passport_number')
        age = data.get('age')
        disabilities = data.get('disabilities')
        Mobile_Number = data.get('Mobile_Number')

        if not all([Email, password, First_name, Last_name, Passport_number, age, disabilities, Mobile_Number]):
            return PassengerView.render_error("Missing required fields"), 400

        passenger = PassengerService.create_passenger(Email, password, First_name, Last_name, Passport_number, age, disabilities, Mobile_Number)
        return PassengerView.render_success('passenger created successfully', passenger.Passenger_ID), 201

    @staticmethod
    def login_passenger():
        data = request.form
        Email = data.get('Email')  
        password = data.get('password')

        if not Email or not password:
            return PassengerView.render_error('email or password is missing.'), 400

        passenger = PassengerService.verify_passenger(Email, password)
        if passenger:
            return render_template('passenger.html'), 200
        return PassengerView.render_error('Invalid Email or password'), 401