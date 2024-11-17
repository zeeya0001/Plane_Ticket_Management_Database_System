from shared.models.flight_model import Flight
from shared.utils.db_utils import db

class FlightService:
    @staticmethod
    def create_flight(Flight_name, Departure_Time, Arrival_Time, Year_of_Services, Airline_name, Origin_AP_name, Destination_AP_name, Flight_type, total_seats_available, Class, Flight_Status, Flight_Location):
        new_flight = Flight(Flight_name=Flight_name, Departure_Time=Departure_Time, Arrival_Time=Arrival_Time, Year_of_Services=Year_of_Services, Airline_name=Airline_name, Origin_AP_name=Origin_AP_name, Destination_AP_name=Destination_AP_name, Flight_type=Flight_type, total_seats_available=total_seats_available, Class=Class, Flight_Status=Flight_Status, Flight_Location=Flight_Location)
        db.session.add(new_flight)
        db.session.commit()
        return new_flight

    @staticmethod
    def get_flight_by_id(Flight_name):
        return Flight.query.get(Flight_name)

    @staticmethod
    def get_all_flights():
        return Flight.query.all()
