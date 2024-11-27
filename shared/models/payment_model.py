from datetime import datetime
from shared.utils.db_utils import db
from shared.models.booking_model import Booking

class Payment(db.Model):
    __tablename__ = 'payment'
    Payment_ID = db.Column(db.Integer, primary_key=True)
    Amount = db.Column(db.Numeric(10, 2), nullable=False)
    Payment_Method = db.Column(db.String(20), nullable=False)
    UPI_ID = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Status = db.Column(db.String(10))
    Booking_ID = db.Column(db.Integer,nullable=False)