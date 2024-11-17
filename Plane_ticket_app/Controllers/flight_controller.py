from flask import request
from Plane_ticket_app.Services.flight_service import FlightService
from Plane_ticket_app.templates.passenger_views import PassengerView

class FlightController:
    @staticmethod
    def get_flight():
        flight_name = request.form.get('Flight_ID')
        flight = FlightService.get_flight_by_Flight_name(Flight_name)
        if not flight: # if flight is None:
            return PassengerView.render_error('flight not found'), 404
        return PassengerView.render_flight(flight), 200

    @staticmethod
    def create_flight():
        data = request.form
        Flight_name = data.get('Flight_name')
        Departure_Time = data.get('Departure_Time')
        Arrival_Time = data.get('Arrival_Time')
        Year_of_Services = data.get('Year_of_Services')
        Airline_name = data.get('Airline_name')
        Origin_AP_name = data.get('Origin_AP_name')
        Destination_AP_name = data.get('Destination_AP_name')
        Flight_type = data.get('Flight_type')
        total_seats_available = data.get('total_seats_available')
        Class = data.get('Class')
        Flight_Status = data.get('Flight_Status')
        Flight_Location = data.get('Flight_Location')

        flight = FlightService.create_flight(Flight_name,  Departure_Time, Arrival_Time, Year_of_Services, Airline_name, Origin_AP_name, Destination_AP_name, Flight_type, total_seats_available, Class, Flight_Status, Flight_Location)
        return PassengerView.render_success('flight created successfully'), 201
