from datetime import datetime
from shared.models.booking_model import Booking
from shared.models.passenger_model import Passenger
from shared.models.flight_model import Flight
from shared.models.payment_model import Payment
from shared.models.cancellation_model import Cancellation
from shared.models.seatMatrix_model import SeatMatrix
from shared.models.service_model import Services
from shared.utils.db_utils import db

class BookingService:
    def book_ticket(Flight_ID, Passenger_ID, Origin_AP_name, Destination_AP_name, Journey_date, Gender, Age, Number_of_seats, Seat_number, Boarding_time, Check_in_time, Class, Status="Booked"):
        
        flight = Flight.query.get(Flight_ID)
        if not flight:
            return {"message": "Flight not found", "status": 404}
        if flight.total_seats_available < Number_of_seats:
            return {"message": "Not enough seats available", "status": 400}

        # Check if passenger exists
        passenger = Passenger.query.get(Passenger_ID)
        if not passenger:
            return {"message": "Passenger not found", "status": 404}

        flight.total_seats_available -= Number_of_seats

        # Create a new booking
        book_ticket = Booking(
            Flight_ID=Flight_ID,
            Passenger_ID=Passenger_ID,
            Origin_AP_name=Origin_AP_name,
            Destination_AP_name=Destination_AP_name,
            Journey_date=Journey_date,
            Gender=Gender,
            Age=Age,
            Number_of_seats=Number_of_seats,
            Seat_number=Seat_number,
            Boarding_time=Boarding_time,
            Check_in_time=Check_in_time,
            Class=Class,
            Status=Status
        )

        # Add the booking and commit to the database
        db.session.add(book_ticket)
        db.session.commit()
        
        return {"message": "Booking successful", "booking_id": booking.Booking_ID}

    @staticmethod
    def get_booking_by_id(Booking_ID):
        return Booking.query.filter_by(Booking_ID=Booking_ID).first()

    @staticmethod
    def get_all_bookings():
        return Booking.query.all()

    @staticmethod
    def cancel_booking(Booking_ID, Request_time, Issue_time, Amount_refunded, Reason):
        booking = Booking.query.get(Booking_ID)
        if booking:
            cancellation = Cancellation(
                Booking_ID=Booking_ID,
                Request_time=Request_time,
                Issue_time=Issue_time,
                Amount_refunded=Amount_refunded,
                Reason=Reason
            )
            db.session.add(cancellation)
            booking.Status = "Cancelled"
            db.session.commit()
            return True
        return False

    @staticmethod
    def process_payment(Booking_ID, Amount, Payment_Method, UPI_ID):
        new_payment = Payment(
            Booking_ID=Booking_ID, 
            Amount=Amount, 
            Payment_Method=Payment_Method,
            UPI_ID = UPI_ID, 
            Status="Pending"
        )
        db.session.add(new_payment)
        db.session.commit()
        new_payment.Status = "Paid"
        db.session.commit()
        return new_payment

    @staticmethod
    def get_payment_status(Booking_ID):
        payment = Payment.query.filter_by(Booking_ID=Booking_ID).first()
        return payment.Status if payment else "No payment found"


    @staticmethod
    def create_service(Service_name, about_service, Airport_ID, Booking_ID):
        new_services = Flight(Service_name=Service_name, about_service=about_service, Airport_ID=Airport_ID, Booking_ID=Booking_ID)
        db.session.add(new_services)
        db.session.commit()
        return new_services

    @staticmethod
    def get_all_services():
        return Services.query.all()
    
    
    @staticmethod
    def update_service(Service_ID, about_service):
        service = Services.query.filter_by(Service_ID=Service_ID, about_service=about_service).first()
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

