from datetime import datetime
from shared.utils.db_utils import db

class Flight(db.Model):
    __tablename__ = 'flight'
    Flight_ID = db.Column(db.Integer, primary_key=True)
    Flight_name = db.Column(db.String(50), nullable=False)
    Departure_Time = db.Column(db.DateTime, nullable=False)
    Arrival_Time = db.Column(db.DateTime, nullable=False)
    Year_of_Services = db.Column(db.Integer, nullable=False)
    Airline_name = db.Column(db.String(50), nullable=False)
    Origin_AP_name = db.Column(db.String(100), nullable=False)
    Destination_AP_name = db.Column(db.String(100), nullable=False)
    Flight_type = db.Column(db.String(20), nullable=False)
    total_seats_available = db.Column(db.Integer, nullable=False)
    Flight_Status = db.Column(db.String(20), nullable=False)
    Date = db.Column(db.Date)
