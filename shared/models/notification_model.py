from datetime import datetime
from shared.utils.db_utils import db
from shared.models.passenger_model import Passenger

class Notification(db.Model):
    __tablename__ = 'notification'
    Notification_ID = db.Column(db.Integer, primary_key=True)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(10), default="unread")
    notification_type = db.Column(db.String(50), nullable=False) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    