from datetime import datetime
from shared.utils.db_utils import db
from shared.models.passenger_model import Passenger
from shared.models.flight_model import Flight

class Review(db.Model):
    __tablename__ = 'review'
    Review_ID = db.Column(db.Integer, primary_key=True)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'), nullable=False)
    Rating = db.Column(db.Integer, nullable=False)
    Content = db.Column(db.String(255), nullable=False)
    Date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    