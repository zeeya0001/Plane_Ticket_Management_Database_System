from datetime import datetime
from shared.utils.db_utils import db

class Passenger(db.Model):
    __tablename__ = 'passenger'
    Passenger_ID = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(20), nullable=False)
    Last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    disabilities = db.Column(db.String(20))
    Mobile_Number = db.Column(db.String(10), unique=True, nullable=False)
    Passport_number = db.Column(db.String(20), nullable=False, unique=True)
    seat_number = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)