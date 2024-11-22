from flask import render_template,request,redirect,url_for

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
        number_of_passengers = int(request.form.get('number_of_passengers', 1))
        
        for _ in range(number_of_passengers):
            First_name = request.form.get('First_name', '')
            Last_name = request.form.get('Last_name', '')
            Passport_number = request.form.get('Passport_number')
            gender = request.form.get('gender')
            age = request.form.get('age')
            disabilities = request.form.get('disabilities')
            Mobile_Number = request.form.get('Mobile_Number')
            seat_number = request.form.get('seat_number')

            if not all([First_name, Last_name, Passport_number, gender, age, disabilities, Mobile_Number, seat_number]):
                return render_template('render.html', message="Missing required fields"), 400

            PassengerService.create_passenger(First_name, Last_name, Passport_number, gender, age, disabilities, Mobile_Number, seat_number)

        return render_template('payment.html', number_of_passengers=number_of_passengers,price=1000*number_of_passengers), 201

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

