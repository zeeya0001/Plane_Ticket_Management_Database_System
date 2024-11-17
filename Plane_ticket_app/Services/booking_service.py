from datetime import datetime
from shared.models.booking_model import Booking
from shared.models.passenger_model import Passenger
from shared.models.flight_model import Flight
from shared.models.payment_model import Payment
from shared.models.cancellation_model import Cancellation
from shared.models.seatMatrix_model import SeatMatrix
from shared.utils.db_utils import db

class BookingService:
    def book_ticket(Flight_ID, Passenger_ID, Origin_AP_name, Destination_AP_name, Journey_date, Gender, Age, Seat_number, Boarding_time, Check_in_time, Class, Price, Status="Booked"):
        
        flight = Flight.query.get(Flight_ID)
        if not flight:
            return {"message": "Flight not found", "status": 404}
        if flight.total_seats_available <= 0:
            return {"message": "No seats available", "status": 400}

        # Check if passenger exists
        passenger = Passenger.query.get(Passenger_ID)
        if not passenger:
            return {"message": "Passenger not found", "status": 404}

        flight.total_seats_available -= 1

        # Create a new booking
        booking = Booking(
            Flight_ID=Flight_ID,
            Passenger_ID=Passenger_ID,
            Origin_AP_name=Origin_AP_name,
            Destination_AP_name=Destination_AP_name,
            Journey_date=Journey_date,
            Gender=Gender,
            Age=Age,
            Seat_number=Seat_number,
            Boarding_time=Boarding_time,
            Check_in_time=Check_in_time,
            Class=Class,
            Price=Price,
            Status=Status
        )

        # Add the booking and commit to the database
        db.session.add(booking)
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
    def process_payment(Booking_ID, Amount, Payment_Method):
        new_payment = Payment(
            Booking_ID=Booking_ID, 
            Amount=Amount, 
            Payment_Method=Payment_Method, 
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
