import random
from flask import request, jsonify, render_template
from datetime import datetime
from Plane_ticket_app.Services.booking_service import BookingService
from Plane_ticket_app.templates.passenger_views import PassengerView
from shared.models.flight_model import Flight
from shared.models.passenger_model import Passenger
from Plane_ticket_app.Services.flight_service import FlightService
from Plane_ticket_app.Services.passenger_services import PassengerService


class BookingController:
    @staticmethod
    def ticket(Flight_ID, no_of_passengers,p_id):
        
        Flight = FlightService.get_flight_by_id(Flight_ID=Flight_ID)
        Passenger = PassengerService.get_passenger_by_Passenger_ID(Passenger_ID=p_id)
        return render_template('ticket.html', flight = Flight, no_of_passengers=no_of_passengers, passenger=Passenger)

    @staticmethod
    def book_ticket():
        Flight_ID = request.form.get('Flight_ID')
        Passenger_ID = request.form.get('Passenger_ID')
        Origin_AP_name = request.form.get('Origin_AP_name')
        Destination_AP_name = request.form.get('Destination_AP_name')
        Journey_date = request.form.get('Journey_date')
        Gender = request.form.get('Gender')
        Age = request.form.get('Age')
        Seat_number = request.form.get('Seat_number')
        Boarding_time = request.form.get('Boarding_time')
        Check_in_time = request.form.get('Check_in_time')
        Class = request.form.get('Class')
        Status = request.form.get('Status')

        if not all([Flight_ID, Passenger_ID, Origin_AP_name, Destination_AP_name, Journey_date, Gender, Age, Seat_number, Boarding_time, Check_in_time, Class, Status]):
            return render_template('render.html', message='Missing required fields'), 400

        booking = BookingService.book_ticket(
            Flight_ID, Passenger_ID, Origin_AP_name, Destination_AP_name, Journey_date, Gender, Age, Seat_number, Boarding_time, Check_in_time, Class, Status
        )
        
        if isinstance(booking, dict):  # Error case
            return render_template('render.html', message=booking["status"]), booking["status"]

        return render_template('render.html', message='Booking created successfully'), 201

    @staticmethod
    def get_booking():
        Booking_ID = request.form.get('Booking_ID')
        booking = BookingService.get_booking_by_id(Booking_ID)
        if not booking:
            return render_template('render.html', message='Booking not found'), 404
        return render_template('get_booking.html', booking=booking), 200

    @staticmethod
    def process_payment(no_of_passengers, Flight_ID, p_id):
        Booking_ID = random.randint(1000, 9999)
        Amount = request.form.get('amount')
        Payment_Method = request.form.get('Payment_Method')
        UPI_ID = request.form.get('UPI_ID')

        if not all([Booking_ID, Amount, Payment_Method, UPI_ID]):
            return render_template('render.html', message='Booking ID, Amount, Payment Method and UPI_ID are required'), 400

        payment = BookingService.process_payment(Booking_ID, Amount, Payment_Method, UPI_ID)
        if payment:
            return render_template('payment_done.html', booking_id=Booking_ID,no_of_passengers=no_of_passengers,Flight_ID=Flight_ID,p_id=p_id), 201

        return render_template('render.html', message='Payment processing failed'), 500

    @staticmethod
    def cancel_booking():
        Booking_ID = request.form.get('Booking_ID')
        Request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Issue_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Amount_refunded = request.form.get('Amount_refunded')
        Reason = request.form.get('Reason')

        if not all([Booking_ID, Request_time, Issue_time, Amount_refunded, Reason]):
            return render_template('render.html', message='Missing required fields'), 400

        if BookingService.cancel_booking(Booking_ID, Request_time, Issue_time, Amount_refunded, Reason):
            return render_template('render.html', message='Booking cancelled successfully'), 200
        return render_template('render.html', message='Booking not found or already cancelled'), 404

    @staticmethod
    def create_service():
        Service_name = request.form.get('Service_name')
        about_service = request.form.get('about_service')
        Airport_ID = request.form.get('Airport_ID')
        Booking_ID = request.form.get('Booking_ID')

        service = BookingService.create_service(Service_name, about_service, Airport_ID, Booking_ID)
        return render_template('render.html', message='Service created successfully'), 201

    @staticmethod
    def get_all_services():
        services = BookingService.get_all_services()
        return render_template('render.html', message='Services retrieved successfully'), 200

    @staticmethod
    def update_service(Service_ID, data):
        service = BookingService.update_service(Service_ID, data)
        if service:
            return render_template('render.html', message='Service updated successfully'), 200
        return render_template('render.html', message='Failed to update service'), 400

    @staticmethod
    def delete_service(Service_ID):
        success = BookingService.delete_service(Service_ID)
        if success:
            return render_template('render.html', message='Service deleted successfully'), 200
        return render_template('render.html', message='Failed to delete service'), 400

