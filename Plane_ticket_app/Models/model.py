from utils.db_utils import db
from datetime import datetime



class Location(db.Model):
    location_ID = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(30))

class Passenger(db.Model):
    Passenger_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_name = db.Column(db.String(20), nullable=False)
    Last_name = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(100), unique=True)
    Passport_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Passenger_Location(db.Model):
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'), primary_key=True)
    location_ID = db.Column(db.Integer, db.ForeignKey('location.location_ID'), primary_key=True)

class ContactN_Number_Passenger(db.Model):
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'), primary_key=True)
    Contact_Number = db.Column(db.String(10))

class Airline(db.Model):
    Airline_ID = db.Column(db.String(15), primary_key=True)
    Airline_name = db.Column(db.String(100), nullable=False)
    Operating_Region = db.Column(db.String(50), nullable=False)

class ContactN_Number_Airline(db.Model):
    Airline_ID = db.Column(db.String(15), db.ForeignKey('airline.Airline_ID'), primary_key=True)
    Contact_Number = db.Column(db.String(10), primary_key=True)

class Airport(db.Model):
    AP_CODE = db.Column(db.String(10), primary_key=True)
    Airport_name = db.Column(db.String(100), nullable=False)
    location_ID = db.Column(db.Integer, db.ForeignKey('location.location_ID'))
    facilities = db.Column(db.String(50), nullable=False)

class Flight(db.Model):
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
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'), primary_key=True)
    location_ID = db.Column(db.Integer, db.ForeignKey('location.location_ID'), primary_key=True)

class Booking(db.Model):
    Booking_ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.DateTime, nullable=False)
    Payment_Status = db.Column(db.String(20))
    Boarding_time = db.Column(db.DateTime)
    ChecK_in_time = db.Column(db.DateTime)
    Price = db.Column(db.Numeric(10, 2))
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'))
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'))

class Services(db.Model):
    Service_ID = db.Column(db.Integer, primary_key=True)
    Service_name = db.Column(db.String(100), nullable=False)
    Airport_ID = db.Column(db.String(3), db.ForeignKey('airport.AP_CODE'))

class Booking_Services(db.Model):
    Booking_ID = db.Column(db.Integer, db.ForeignKey('booking.Booking_ID'), primary_key=True)
    Service_ID = db.Column(db.Integer, db.ForeignKey('services.Service_ID'), primary_key=True)

class Seat_Matrix(db.Model):
    Seat_ID = db.Column(db.Integer, primary_key=True)
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'))
    Seat_Number = db.Column(db.String(5), nullable=False)
    Class = db.Column(db.String(20))
    Availability = db.Column(db.String(10), nullable=False)

class Payment(db.Model):
    Payment_ID = db.Column(db.Integer, primary_key=True)
    Amount = db.Column(db.Numeric(10, 2))
    Payment_Method = db.Column(db.String(20))
    Date = db.Column(db.DateTime)
    Booking_ID = db.Column(db.Integer, db.ForeignKey('booking.Booking_ID'))

class Review(db.Model):
    Review_ID = db.Column(db.Integer, primary_key=True)
    Flight_ID = db.Column(db.Integer, db.ForeignKey('flight.Flight_ID'))
    Service_ID = db.Column(db.Integer, db.ForeignKey('services.Service_ID'))
    Rating = db.Column(db.Integer)
    Date = db.Column(db.DateTime)
    Comment = db.Column(db.String(255))
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'))

class Notification(db.Model):
    Notification_ID = db.Column(db.Integer, primary_key=True)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('passenger.Passenger_ID'))
    Message = db.Column(db.String(255))
    Date = db.Column(db.DateTime)

class Cancellation(db.Model):
    Cancellation_ID = db.Column(db.Integer, primary_key=True)
    Booking_ID = db.Column(db.Integer, db.ForeignKey('booking.Booking_ID'))
    Request_time = db.Column(db.DateTime, nullable=False)
    Issue_time = db.Column(db.DateTime, nullable=False)
    Reason = db.Column(db.String(255))

