from shared.utils.db_utils import db
from shared.models.passenger_model import Passenger
from shared.models.flight_model import Flight

class SeatMatrix(db.Model):
    __tablename__ = 'seat_matrix'
    
    seat_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'), nullable=False)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'), nullable=True)  # Allow null for available seats
    seat_number = db.Column(db.String(5), nullable=False)
    seat_class = db.Column(db.String(20), nullable=False)
    
    # Add a unique constraint to ensure no duplicate seat numbers within the same flight
    __table_args__ = (
        db.UniqueConstraint('flight_id', 'seat_number', name='unique_flight_seat'),
    )