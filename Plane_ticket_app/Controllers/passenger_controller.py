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

        form_data = request.form
        First_name = form_data.get('First_name', '').strip()
        Last_name = form_data.get('Last_name', '').strip()
        Passport_number = form_data.get('Passport_number')
        gender = form_data.get('gender')
        age = form_data.get('age')
        disabilities = form_data.get('disabilities', 'None')  # Default to 'None' if not specified
        Mobile_Number = form_data.get('Mobile_Number')
        S_no = form_data.get('S_no')

        if not all([First_name, Last_name, Passport_number, gender, age, disabilities, Mobile_Number]):
            return render_template('render.html', message="Missing required fields"), 400

        PassengerService.create_passenger(First_name=First_name, Last_name=Last_name, Passport_number=Passport_number, gender=gender, age=age, disabilities=disabilities, Mobile_Number=Mobile_Number, Seat_number=S_no)

        passengers = PassengerService.get_all_passengers()
        passengers.sort(key=lambda x: x.Passenger_ID, reverse=True)  # Sort by ID in descending order
        newest_passenger_id = passengers[0].Passenger_ID if passengers else None

        return render_template('payment.html', no_of_passengers=no_of_passengers, price=1000*no_of_passengers, Flight_ID=Flight_ID,p_id=newest_passenger_id), 201

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

