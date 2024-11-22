from datetime import datetime
from shared.utils.db_utils import db
from shared.models.passenger_model import Passenger
from shared.models.flight_model import Flight

class Booking(db.Model):
    __tablename__ = 'booking'
    Booking_ID = db.Column(db.Integer, primary_key=True)
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'), nullable=False)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'), nullable=False)
    Origin_AP_name = db.Column(db.String(100), nullable=False)
    Destination_AP_name = db.Column(db.String(100), nullable=False)
    Journey_date = db.Column(db.DATE, nullable = False)
    Gender = db.Column(db.String(7), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Number_of_seats = db.Column(db.Integer, nullable=False)
    Seat_number = db.Column(db.String(10), unique=True, nullable=False)
    Boarding_time = db.Column(db.DateTime, nullable=True)
    Check_in_time = db.Column(db.DateTime, nullable=True)
    Class = db.Column(db.String(10), nullable=False)
    Price = db.Column(db.Numeric(10, 2), nullable=False)
    Status = db.Column(db.String(20), default='Booked')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

   