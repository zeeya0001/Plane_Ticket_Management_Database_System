from flask import render_template,request,redirect,url_for
from Plane_ticket_app.Services.passenger_services import PassengerService

class PassengerController:
    @staticmethod
    def get_passenger(Passenger_ID):
        passenger = PassengerService.get_passenger_by_Passenger_ID(Passenger_ID)
        if not passenger: 
            return render_template('render.html', message='passenger not found'), 404
        return render_template('passenger_view.html', passenger=passenger), 200

    @staticmethod
    def get_all_passengers():
        passengers = PassengerService.get_all_passengers()
        if not passengers: 
            return render_template('render.html', message='passengers not found'), 404
        return render_template('passenger_view.html', passengers=passengers), 200

    @staticmethod
    def create_passenger():
        no_of_passengers = int(request.args.get('no_of_passengers', 1))
        Flight_ID = request.args.get('Flight_ID')

        for i in range(1,no_of_passengers):
            First_name = request.form.get('First_name_{i}', '')
            Last_name = request.form.get('Last_name_{i}', '')
            Passport_number = request.form.get('Passport_number_{i}')
            gender = request.form.get('gender_{i}')
            age = request.form.get('age_{i}')
            disabilities = request.form.get('disabilities_{i}')
            Mobile_Number = request.form.get('Mobile_Number_{i}')
            seat_number = request.form.get('seat_number_{i}')

            if not all([First_name, Last_name, Passport_number, gender, age, disabilities, Mobile_Number, seat_number]):
                return render_template('render.html', message="Missing required fields"), 400

            PassengerService.create_passenger(First_name, Last_name, Passport_number, gender, age, disabilities, Mobile_Number, seat_number)

        return render_template('payment.html', no_of_passengers=no_of_passengers, price=1000*no_of_passengers, Flight_ID=Flight_ID), 201

    @staticmethod
    def login_passenger():
        Email = request.form.get('Email')  
        password = request.form.get('password')

        if not Email or not password:
            return render_template('render.html', message='Email and password are required'), 400

        passenger = PassengerService.verify_passenger(Email, password)
        if passenger:
            return render_template('render.html', message='Login successful'), 200
        return render_template('render.html', message='Invalid Email or password'), 401

