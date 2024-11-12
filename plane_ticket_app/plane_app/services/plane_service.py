from shared.models.plane_model import Passenger, Flight, Booking, Services, Booking_Services, Seat_Matrix, Payment, Review, Notification, Cancellation
from shared.utils.db_utils import db
from datetime import datetime


class PassengerService:
    @staticmethod
    def create_passenger(data):
        new_passenger = Passenger(
            First_name=data['First_name'],
            Last_name=data['Last_name'],
            Email=data['Email'],
            Passport_number=data['Passport_number'],
            Age=data['Age'],
            disabilities=data['disabilities'],
            Contact_number=data['Contact_number']
        )
        db.session.add(new_passenger)
        db.session.commit()
        return new_passenger

    @staticmethod
    def get_all_passengers():
        return Passenger.query.order_by(Passenger.created_at.desc()).all()

    @staticmethod
    def get_passenger_by_id(Passenger_ID):
        return Passenger.query.filter_by(Passenger_ID=Passenger_ID).first()

    @staticmethod
    def update_passenger(Passenger_ID, data):
        passenger = Passenger.query.filter_by(Passenger_ID=Passenger_ID).first()
        if passenger:
            for key, value in data.items():
                setattr(passenger, key, value)
            db.session.commit()
            return passenger
        return None
    
    @staticmethod
    def delete_passenger(Passenger_ID):
        passenger = Passenger.query.filter_by(Passenger_ID=Passenger_ID).first()
        if passenger:
            db.session.delete(passenger)
            db.session.commit()
            return True
        return False

class FlightService:

    @staticmethod
    def create_flight(data):
        new_flight = Flight(
            Flight_name=data['Flight_name'],
            Departure_Time=data['Departure_Time'],
            Arrival_Time=data['Arrival_Time'],
            Year_of_Searvices=data['Year_of_Searvices'],
            Airline_ID=data['Airline_ID'],
            Origin_AP_CODE=data['Origin_AP_CODE'],
            Destination_AP_CODE=data['Destination_AP_CODE'],
            Flight_Type=data['Flight_Type'],
            Flight_Status=data['Flight_Status']
        )
        db.session.add(new_flight)
        db.session.commit()
        return new_flight

    @staticmethod
    def get_flights_by_id(Flight_ID):
        return Flight.query.filter_by(Flight_ID=Flight_ID).first()
    
    @staticmethod
    def get_flights_by_origin_dest(Origin_AP_CODE, Destination_AP_CODE):
        return Flight.query.filter_by(Origin_AP_CODE=Origin_AP_CODE, Destination_AP_CODE=Destination_AP_CODE).first()

    @staticmethod
    def check_availability(Flight_ID):
        seats = Seat_Matrix.query.filter_by(Flight_ID=Flight_ID, Availability="Available").count()
        return seats > 0

    @staticmethod
    def get_flights_by_departuretime(Departure_Time):
        return Flight.query.filter_by(Departure_Time=Departure_Time).first()

    @staticmethod
    def get_flights_by_arrivaltime(Arrival_Time):
        return Flight.query.filter_by(Arrival_Time=Arrival_Time).first()
    
    @staticmethod
    def update_flight(Flight_ID, data):
        flight = Flight.query.filter_by(Flight_ID=Flight_ID).first()
        if flight:
            for key, value in data.items():
                setattr(flight, key, value)
            db.session.commit()
            return flight
        return None
    
    @staticmethod
    def delete_flight(Flight_ID):
        flight = Flight.query.filter_by(Flight_ID=Flight_ID).first()
        if flight:
            db.session.delete(flight)
            db.session.commit()
            return True
        return False 

class BookingService:
    @staticmethod
    def create_booking(data):
        new_booking = Booking(
            Date=datetime.now(),
            Boarding_time=data['Boarding_time'],
            ChecK_in_time=data['ChecK_in_time'],
            Price=data['Price'],
            Passenger_ID=data['Passenger_ID'],
            Flight_ID=data['Flight_ID'],
            Payment_Status=data.get('Payment_Status', 'Pending'),
            Booking_Status=data.get('Booking_Status', 'Confirmed')
        )
        db.session.add(new_booking)
        db.session.commit()
        return new_booking
    
    @staticmethod
    def get_bookings_by_passenger(Passenger_ID):
        return Booking.query.filter_by(Passenger_ID=Passenger_ID).all()
    
    @staticmethod
    def update_booking_status(Booking_ID, status):
        booking = Booking.query.filter_by(Booking_ID=Booking_ID).first()
        if booking:
            booking.Booking_Status = status
            db.session.commit()
            return booking
        return None
    
    @staticmethod
    def cancel_booking(Booking_ID):
        return CancellationService.create_cancellation({'Booking_ID': Booking_ID, 'Request_time':datetime.now()})
    

class AirportServiceService:
    @staticmethod
    def get_all_services():
        return Services.query.all()
    
    @staticmethod
    def add_service(data):
        new_service = Services(
            Service_name=data['Service_name'],
            Airpot_ID=data['Airpot_ID']
        )
        db.session.add(new_service)
        db.session.commit()
        return new_service
    
    @staticmethod
    def update_service(Service_ID, data):
        service = Services.query.filter_by(Service_ID=Service_ID).first()
        if service:
            for key, value in data.items():
                setattr(service, key, value)
            db.session.commit()
            return service
        return None
    
    @staticmethod
    def delete_service(Service_ID):
        service = Services.query.filter_by(Service_ID=Service_ID).first()
        if service:
            db.session.delete(service)
            db.session.commit()
            return True
        return False

class SeatMatrixService:
    @staticmethod
    def get_seats_for_flight(Flight_ID):
        return Seat_Matrix.query.filter_by(Flight_ID=Flight_ID).all()
    
    @staticmethod
    def mark_seat_as_booked(Seat_ID):
        seat = Seat_Matrix.query.filter_by(Seat_ID=Seat_ID).first()
        if seat and seat.Availability == "Available":
            seat.Availability = "Booked"
            db.session.commit()
            return seat
        return None
    
    @staticmethod
    def release_seat(Seat_ID):
        seat = Seat_Matrix.query.filter_by(Seat_ID=Seat_ID).first()
        if seat and seat.Availability == "Booked":
            seat.Availability = "Available"
            db.session.commit()
            return seat
        return None

class PaymentService:
    @staticmethod
    def create_payment(data):
        new_payment = Payment(
            Amount=data['Amount'],
            Payment_Method=data['Payment_Method'],
            Date=datetime.now(),
            Booking_ID=data['Booking_ID']
        )
        db.session.add(new_payment)
        db.session.commit()
        return new_payment
    
    @staticmethod
    def update_payment_status(Payment_ID, status):
        payment = Payment.query.filter_by(Payment_ID=Payment_ID).first()
        if payment:
            payment.Payment_Status = status
            db.session.commit()
            return payment
        return None

class ReviewService:
    @staticmethod
    def create_review(data):
        new_review = Review(
            Flight_ID=data['Flight_ID'],
            Service_ID=data['Service_ID'],
            Rating=data['Rating'],
            Date=datetime.now(),
            Comment=data['Comment'],
            Passenger_ID=data['Passenger_ID']
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review
    
    @staticmethod
    def get_reviews_by_flight(Flight_ID):
        return Review.query.filter_by(Flight_ID=Flight_ID).all()

class NotificationService:
    @staticmethod
    def create_notification(data):
        new_notification = Notification(
            Passenger_ID=data['Passenger_ID'],
            Message=data['Message'],
            Date=datetime.now(),
            Notification_Type=data['Notification_Type']
        )
        db.session.add(new_notification)
        db.session.commit()
        return new_notification
    
    @staticmethod
    def filter_notifications(Passenger_ID, Notification_Type=None):
        query = Notification.query.filter_by(Passenger_ID=Passenger_ID)
        if Notification_Type:
            query = query.filter_by(Notification_Type=Notification_Type)
        return query.all()

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
    
    @staticmethod
    def calculate_cancellation_fee(Booking_ID):
        booking = Booking.query.filter_by(Booking_ID=Booking_ID).first()
        if booking:
            time_difference = booking.Boarding_time - datetime.now()
            if time_difference > 7:
                return 0
            elif time_difference > 1:
                return booking.Price * 0.25
            else:
                return booking.Price * 0.5
        return None