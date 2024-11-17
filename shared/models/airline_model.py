from shared.utils.db_utils import db

class Airline(db.Model):
    __tablename__ = 'airline'
    Airline_ID = db.Column(db.String(15), primary_key=True)
    Years_of_Service = db.Column(db.Integer, nullable=False)
    Airline_name = db.Column(db.String(100), nullable=False)
    Operating_Region = db.Column(db.String(50), nullable=False)
    Contact_number = db.Column(db.String(10), unique=True, nullable=False)

    