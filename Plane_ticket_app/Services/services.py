from Plane_ticket_app.Models.model import Passenger, Flight, Booking, Services, Booking_Services, Seat_Matrix, Payment, Review, Notification, Cancellation
from utils.db_utils import db


class PassengerService:
    @staticmethod
    def create_passenger(data):
        new_passenger = Passenger(
            First_name=data['First_name'],
            Last_name=data['Last_name'],
            Email=data['Email'],
            Passport_number=data['Passport_number']
        )
        db.session.add(new_passenger)
        db.session.commit()
        return new_passenger

    @staticmethod
    def get_all_passengers():
        return Passenger.query.all()

class FlightService:
    @staticmethod
    def get_all_flights():
        return Flight.query.all()

class BookingService:
    @staticmethod
    def create_booking(data):
        new_booking = Booking(
            Booking_time=data['Booking_time'],
            Boarding_time=data['Boarding_time'],
            ChecK_in_time=data['ChecK_in_time'],
            Price=data['Price'],
            Passenger_ID=data['Passenger_ID'],
            Flight_ID=data['Flight_ID']
        )
        db.session.add(new_booking)
        db.session.commit()
        return new_booking

class AirportServiceService:
    @staticmethod
    def get_all_services():
        return Services.query.all()

class SeatMatrixService:
    @staticmethod
    def get_seats_for_flight(flight_id):
        return Seat_Matrix.query.filter_by(Flight_ID=flight_id).all()

class PaymentService:
    @staticmethod
    def create_payment(data):
        new_payment = Payment(
            Amount=data['Amount'],
            Payment_Method=data['Payment_Method'],
            Date=data['Date'],
            Booking_ID=data['Booking_ID']
        )
        db.session.add(new_payment)
        db.session.commit()
        return new_payment

class ReviewService:
    @staticmethod
    def create_review(data):
        new_review = Review(
            Flight_ID=data['Flight_ID'],
            Service_ID=data['Service_ID'],
            Rating=data['Rating'],
            Date=data['Date'],
            Comment=data['Comment'],
            Passenger_ID=data['Passenger_ID']
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review

class NotificationService:
    @staticmethod
    def create_notification(data):
        new_notification = Notification(
            Passenger_ID=data['Passenger_ID'],
            Message=data['Message'],
            Date=data['Date']
        )
        db.session.add(new_notification)
        db.session.commit()
        return new_notification

class CancellationService:
    @staticmethod
    def create_cancellation(data):
        new_cancellation = Cancellation(
            Booking_ID=data['Booking_ID'],
            Request_time=data['Request_time'],
            Issue_time=data['Issue_time'],
            Reason=data['Reason']
        )
        db.session.add(new_cancellation)
        db.session.commit()
        return new_cancellation
