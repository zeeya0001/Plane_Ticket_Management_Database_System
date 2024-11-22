from shared.utils.db_utils import db
from shared.models.airport_model import Airport
from shared.models.booking_model import Booking
class Services(db.Model):
    __tablename__ = 'services'
    Service_ID = db.Column(db.Integer, primary_key=True)
    Service_name = db.Column(db.String(30), nullable=False)
    about_service = db.Column(db.String(100))
    Airport_ID = db.Column(db.String(10), db.ForeignKey('airport.AP_CODE'), nullable=False)
    Booking_ID = db.Column(db.Integer, db.ForeignKey('booking.Booking_ID'), nullable=False)

   