from flask import render_template
from shared.models.flight_model import Flight
from shared.utils.db_utils import db

class FlightService:
    @staticmethod
    def create_flight(Flight_name, Departure_Time, Arrival_Time, Year_of_Services, Airline_name, Origin_AP_name, Destination_AP_name, Flight_type, total_seats_available, Flight_Status,Date):
        new_flight = Flight(Flight_name=Flight_name, Departure_Time=Departure_Time, Arrival_Time=Arrival_Time, Year_of_Services=Year_of_Services, Airline_name=Airline_name, Origin_AP_name=Origin_AP_name, Destination_AP_name=Destination_AP_name, Flight_type=Flight_type, total_seats_available=total_seats_available, Flight_Status=Flight_Status, Date=Date)

        db.session.add(new_flight)
        db.session.commit()
        return new_flight

    @staticmethod
    def get_flight_by_id(Flight_ID):
        return Flight.query.filter_by(Flight_ID=Flight_ID).first()

    @staticmethod
    def get_flight_by_flight_name(Flight_name):
        return Flight.query.filter_by(Flight_name=Flight_name).first()

    @staticmethod
    def get_flight_by_Origin_and_Destination_AP_name(Origin_AP_name, Destination_AP_name,Date):
        return Flight.query.filter_by(Origin_AP_name=Origin_AP_name, Destination_AP_name=Destination_AP_name,Date=Date).all()

    @staticmethod
    def get_all_flights():
        return Flight.query.all()
