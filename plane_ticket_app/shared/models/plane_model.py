from shared.utils.db_utils import db
from datetime import datetime

class Location(db.Model):
    __tablename__ = 'location'

    location_ID = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(30), nullable=False)

class Passenger(db.Model):
    __tablename__ = 'passengers'

    Passenger_ID = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(20), nullable=False)
    Last_name = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(100), unique=True)
    Passport_number = db.Column(db.String(20), unique=True, nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    disabilities = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    location_ID = db.Column(db.Integer, db.ForeignKey('location.location_ID'), nullable=False)
    Contact_Number = db.Column(db.String(15), nullable=False)

class Airline(db.Model):
    __tablename__ = 'airline'

    Airline_ID = db.Column(db.String(15), primary_key=True)
    Airline_name = db.Column(db.String(100), nullable=False)
    Operating_Region = db.Column(db.String(50), nullable=False)
    Contact_Number = db.Column(db.String(15), nullable=False)

class Airport(db.Model):
    __tablename__ = 'airpot'

    AP_CODE = db.Column(db.String(10), primary_key=True)
    Airport_name = db.Column(db.String(100), nullable=False)
    location_ID = db.Column(db.Integer, db.ForeignKey('location.location_ID'))
    facilities = db.Column(db.String(50), nullable=False)

class Flight(db.Model):
    __tablename__ = 'flight'
    
    Flight_ID = db.Column(db.Integer, primary_key=True)
    Flight_name = db.Column(db.String(20), nullable=False)
    Departure_Time = db.Column(db.DateTime, nullable=False)
    Arrival_Time = db.Column(db.DateTime, nullable=False)
    Year_of_Services = db.Column(db.Integer, nullable=False)
    Airline_ID = db.Column(db.String(15), db.ForeignKey('airline.Airline_ID'))
    Origin_AP_CODE = db.Column(db.String(10), db.ForeignKey('airport.AP_CODE'))
    Destination_AP_CODE = db.Column(db.String(10), db.ForeignKey('airport.AP_CODE'))
    Flight_type = db.Column(db.String(20), nullable=False)
    Flight_Status = db.Column(db.String(20), nullable=False)

class Flight_Location(db.Model):
    __tablename__ = 'flight_location'

    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'), primary_key=True)
    location_ID = db.Column(db.Integer, db.ForeignKey('location.location_ID'), primary_key=True)

class Booking(db.Model):
    __tablename__ = 'bookings'

    Booking_ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.DateTime, nullable=False)
    Payment_Status = db.Column(db.String(20))
    Boarding_time = db.Column(db.DateTime)
    ChecK_in_time = db.Column(db.DateTime)
    Price = db.Column(db.Numeric(10, 2))
    Booking_Type = db.Column(db.String(20), nullable=True)
    Booking_Status = db.Column(db.String(20), nullable=True)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passengers.Passenger_ID'))
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'))

class Services(db.Model):
    __tablename__ = 'services'

    Service_ID = db.Column(db.Integer, primary_key=True)
    Service_name = db.Column(db.String(100), nullable=False)
    Airport_ID = db.Column(db.String(3), db.ForeignKey('airport.AP_CODE'))

class Booking_Services(db.Model):
    __tablename__ = 'booking_services'

    Booking_ID = db.Column(db.Integer, db.ForeignKey('bookings.Booking_ID'), primary_key=True)
    Service_ID = db.Column(db.Integer, db.ForeignKey('services.Service_ID'), primary_key=True)

class Seat_Matrix(db.Model):
    __tablename__ = 'seat_matrix'

    Seat_ID = db.Column(db.Integer, primary_key=True)
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'))
    Seat_Number = db.Column(db.String(5), nullable=False)
    Class = db.Column(db.String(20))
    Availability = db.Column(db.String(10), nullable=False)

class Payment(db.Model):
    __tablename__ = 'payment'

    Payment_ID = db.Column(db.Integer, primary_key=True)
    Amount = db.Column(db.Numeric(10, 2))
    Payment_Method = db.Column(db.String(20))
    Date = db.Column(db.DateTime)
    Payment_Status = db.Column(db.String(20), nullable=False)
    Booking_ID = db.Column(db.Integer, db.ForeignKey('bookings.Booking_ID'))

class Review(db.Model):
    __tablename__ = 'reviews'

    Review_ID = db.Column(db.Integer, primary_key=True)
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'))
    Service_ID = db.Column(db.Integer, db.ForeignKey('services.Service_ID'))
    Rating = db.Column(db.Integer)
    Date = db.Column(db.DateTime)
    Comment = db.Column(db.String(255))
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passengers.Passenger_ID'))

class Notification(db.Model):
    __tablename__ = 'notifications'

    Notification_ID = db.Column(db.Integer, primary_key=True)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passengers.Passenger_ID'))
    Message = db.Column(db.String(255))
    Date = db.Column(db.DateTime)
    Notification_Type = db.Column(db.String(20))

class Cancellation(db.Model):
    __tablename__ = 'cancellation'

    Cancellation_ID = db.Column(db.Integer, primary_key=True)
    Booking_ID = db.Column(db.Integer, db.ForeignKey('bookings.Booking_ID'))
    Request_time = db.Column(db.DateTime, nullable=False)
    Issue_time = db.Column(db.DateTime, nullable=False)
    Reason = db.Column(db.String(255))
