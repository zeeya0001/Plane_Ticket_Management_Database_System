from flask import request, jsonify
from datetime import datetime
from Plane_ticket_app.Services.booking_service import BookingService
from Plane_ticket_app.templates.passenger_views import PassengerView

class BookingController:
    @staticmethod
    def book_ticket():
        data = request.form
        print(data)  # Debug: Log the received payload to identify missing fields

        Flight_ID = data.get('Flight_ID')
        Passenger_ID = data.get('Passenger_ID')
        Origin_AP_name = data.get('Origin_AP_name')
        Destination_AP_name = data.get('Destination_AP_name')
        Journey_date = data.get('Journey_date')
        Gender = data.get('Gender')
        Age = data.get('Age')
        Seat_number = data.get('Seat_number')
        Boarding_time = data.get('Boarding_time')
        Check_in_time = data.get('Check_in_time')
        Class = data.get('Class')
        Price = data.get('Price')
        Status = data.get('Status')

        # Validate missing fields
        if not all([Flight_ID, Passenger_ID,  Origin_AP_name, Destination_AP_name, Journey_date,  Gender, Age, Seat_number, Boarding_time, Check_in_time, Class, Price, Status]):
            return PassengerView.render_error('Missing required fields'), 400

        # Book ticket
        booking = BookingService.book_ticket(
            Flight_ID, Passenger_ID, Origin_AP_name, Destination_AP_name, Journey_date, Gender, Age, Seat_number,  Boarding_time, Check_in_time, Class, float(Price), Status 
        )
            
        if isinstance(booking, dict):  # Error case
            return PassengerView.render_error(booking["message"]), booking["status"]

        return PassengerView.render_success('Booking created successfully', booking_id=booking.Booking_ID), 201

    @staticmethod
    def get_booking():
        Booking_ID = request.form.get('Booking_ID')
        booking = BookingService.get_booking_by_id(Booking_ID)
        if not booking:
            return PassengerView.render_error('Booking not found'), 404
        return PassengerView.render_booking(booking), 200

    @staticmethod
    def process_payment():
        data = request.form
        Booking_ID = data.get('Booking_ID')
        Amount = data.get('Amount')
        Payment_Method = data.get('Payment_Method')

        if not all([Booking_ID, Amount, Payment_Method]):
            return PassengerView.render_error('Booking ID, Amount and Payment Method are required'), 400

       
        payment = BookingService.process_payment(Booking_ID, Amount, Payment_Method)
        if payment:
            return PassengerView.render_success('Payment processed successfully'), 201
        return PassengerView.render_error('Payment processing failed'), 500

    @staticmethod
    def cancel_booking():
        data = request.form
        Booking_ID = data.get('Booking_ID')
        Request_time = data.get('Request_time')
        Issue_time = data.get('Issue_time')
        Amount_refunded = data.get('Amount_refunded')
        Reason = data.get('Reason')

        if not all([Booking_ID, Request_time, Issue_time, Amount_refunded, Reason]):
            return PassengerView.render_error('Missing required fields'), 400

        if BookingService.cancel_booking(Booking_ID, Request_time, Issue_time, Amount_refunded, Reason):
            return PassengerView.render_success('Booking cancelled successfully'), 200
        return PassengerView.render_error('Booking not found or already cancelled'), 404