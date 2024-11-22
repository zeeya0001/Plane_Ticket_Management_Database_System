from flask import render_template,request,redirect,url_for
from Plane_ticket_app.Services.flight_service import FlightService
from Plane_ticket_app.templates.passenger_views import PassengerView

class FlightController:
    @staticmethod
    def get_flight_by_Flight_name(Flight_name):
        flight = FlightService.get_flight_by_Flight_name(Flight_name)
        if not flight: # if flight is None:
            return render_template('render.html', message='No flights found for the given name'), 404
        return render_template('get_flight.html', flight=flight), 200

    @staticmethod
    def get_flight_by_id(Flight_ID):
        flight = FlightService.get_flight_by_id(Flight_ID)
        if not flight: # if flight is None:
            return render_template('render.html', message='No flights found for the given id'), 404
        return render_template('render.html', message=PassengerView.render_flight(flight)), 200

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
        Flight_Status = data.get('Flight_Status')
        Date=data.get('Date')

        flight = FlightService.create_flight(Flight_name,  Departure_Time, Arrival_Time, Year_of_Services, Airline_name, Origin_AP_name, Destination_AP_name, Flight_type, total_seats_available, Flight_Status, Date)
        return render_template('render.html', message=PassengerView.render_success('flight created successfully')), 201
    @staticmethod
    def get_flight_by_Origin_and_Destination_AP_name(Origin_AP_name, Destination_AP_name,Date, no_of_passengers):
        flights = FlightService.get_flight_by_Origin_and_Destination_AP_name(Origin_AP_name, Destination_AP_name,Date)
        if not flights: # if flight is None:
            return render_template('render.html', message='No flights found for the given origin and destination or date'), 404
        if len(flights) > 0:
            return render_template('get_flight.html',flight=flights[0],no_of_passengers=no_of_passengers), 200

