from datetime import datetime
from shared.utils.db_utils import db
from shared.models.booking_model import Booking

class Cancellation(db.Model):
    __tablename__ = 'cancellation'
    Cancellation_ID = db.Column(db.Integer, primary_key=True)
    Booking_ID = db.Column(db.Integer, db.ForeignKey('booking.Booking_ID'), nullable=False)
    Request_time = db.Column(db.DateTime, nullable=False)
    Issue_time = db.Column(db.DateTime, nullable=False)
    Amount_refunded = db.Column(db.Integer, nullable=False)
    Reason = db.Column(db.String(255), nullable=False)

    