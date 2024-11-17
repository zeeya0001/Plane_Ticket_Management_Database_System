from datetime import datetime
from shared.utils.db_utils import db

class Passenger(db.Model):
    __tablename__ = 'passenger'
    Passenger_ID = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(20), nullable=False)
    Last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    disabilities = db.Column(db.String(20))
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Mobile_Number = db.Column(db.String(10), unique=True, nullable=False)
    Passport_number = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    