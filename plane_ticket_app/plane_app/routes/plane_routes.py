from flask import Blueprint, request, jsonify
from plane_app.controllers.plane_controller import (
    PassengerController, FlightController, BookingController, 
    ServiceController, SeatMatrixController, PaymentController, 
    ReviewController, NotificationController, CancellationController
)

plane_bp = Blueprint('plane_bp', __name__)

@plane_bp.route('/api/passengers', methods=['POST'])
def create_passenger():
    data = request.get_json()
    result = PassengerController.create_passenger(data)
    return jsonify(result)

@plane_bp.route('/api/passengers', methods=['GET'])
def get_all_passengers():
    result = PassengerController.get_all_passengers()
    return jsonify(result)

@plane_bp.route('/api/passengers/<int:Passenger_ID>', methods=['GET'])
def get_passenger_by_id(Passenger_ID):
    result = PassengerController.get_passenger_by_id(Passenger_ID)
    return jsonify(result)

@plane_bp.route('/api/passengers/<int:Passenger_ID>', methods=['PUT'])
def update_passenger(Passenger_ID):
    data = request.get_json()
    result = PassengerController.update_passenger(Passenger_ID, data)
    return jsonify(result)

@plane_bp.route('/api/passengers/<int:Passenger_ID>', methods=['DELETE'])
def delete_passenger(Passenger_ID):
    result = PassengerController.delete_passenger(Passenger_ID)
    return jsonify(result)

@plane_bp.route('/api/flights', methods=['POST'])
def create_flight():
    data = request.get_json()
    result = FlightController.create_flight(data)
    return jsonify(result)

@plane_bp.route('/api/flights/<int:Flight_ID>', methods=['GET'])
def get_flight_by_id(Flight_ID):
    result = FlightController.get_flight_by_id(Flight_ID)
    return jsonify(result)

@plane_bp.route('/api/flights/origin/<string:origin_ap_code>/destination/<string:destination_ap_code>', methods=['GET'])
def get_flights_by_origin_dest(Origin_AP_CODE, Destination_AP_CODE):
    result = FlightController.get_flights_by_origin_dest(Origin_AP_CODE, Destination_AP_CODE)
    return jsonify(result)

@plane_bp.route('/api/flights/<int:flight_id>/availability', methods=['GET'])
def check_availability(Flight_ID):
    result = FlightController.check_availability(Flight_ID)
    return jsonify(result)

@plane_bp.route('/api/flights/departure/<string:Departure_Time>', methods=['GET'])
def get_flights_by_departure_time(Departure_Time):
    result = FlightController.get_flights_by_departure_time(Departure_Time)
    return jsonify(result)

@plane_bp.route('/api/flights/arrival/<string:Arrival_Time>', methods=['GET'])
def get_flights_by_arrival_time(Arrival_Time):
    result = FlightController.get_flights_by_arrival_time(Arrival_Time)
    return jsonify(result)

@plane_bp.route('/api/flights/<int:Flight_ID>', methods=['PUT'])
def update_flight(Flight_ID):
    result = FlightController.update_flight(Flight_ID)
    return jsonify(result)

@plane_bp.route('/api/flights/<int:Flight_ID>', methods=['DELETE'])
def delete_flight(Flight_ID):
    result = FlightController.delete_flight(Flight_ID)
    return jsonify(result)

@plane_bp.route('/api/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    result = BookingController.create_booking(data)
    return jsonify(result)

@plane_bp.route('/api/bookings/passenger/<int:Passenger_ID>', methods=['GET'])
def get_bookings_by_passenger(Passenger_ID):
    result = BookingController.get_bookings_by_passenger(Passenger_ID)
    return jsonify(result)

@plane_bp.route('/api/bookings/<int:Booking_ID>/status', methods=['PUT'])
def update_booking_status(Booking_ID):
    status = request.json.get("status")
    result = BookingController.update_booking_status(Booking_ID, status)
    return jsonify(result)

@plane_bp.route('/api/bookings/<int:Booking_ID>/cancel', methods=['POST'])
def cancel_booking(Booking_ID):
    result = BookingController.cancel_booking(Booking_ID)
    return jsonify(result)

@plane_bp.route('/api/services', methods=['POST'])
def add_service():
    data = request.get_json()
    result = ServiceController.add_service(data)
    return jsonify(result)

@plane_bp.route('/api/services', methods=['GET'])
def get_all_services():
    result = ServiceController.get_all_services()
    return jsonify(result)

@plane_bp.route('/api/services/<int:Service_ID>', methods=['PUT'])
def update_service(Service_ID):
    data = request.get_json()
    result = ServiceController.update_service(Service_ID, data)
    return jsonify(result)

@plane_bp.route('/api/services/<int:Service_ID>', methods=['DELETE'])
def delete_service(Service_ID):
    result = ServiceController.delete_service(Service_ID)
    return jsonify(result)

@plane_bp.route('/api/seats/flight/<int:Flight_ID>', methods=['GET'])
def get_seats_for_flight(Flight_ID):
    result = SeatMatrixController.get_seats_for_flight(Flight_ID)
    return jsonify(result)

@plane_bp.route('/api/seats/<int:Seat_ID>/book', methods=['POST'])
def mark_seat_as_booked(Seat_ID):
    result = SeatMatrixController.mark_seat_as_booked(Seat_ID)
    return jsonify(result)

@plane_bp.route('/api/seats/<int:Seat_ID>/release', methods=['POST'])
def release_seat(Seat_ID):
    result = SeatMatrixController.release_seat(Seat_ID)
    return jsonify(result)

@plane_bp.route('/api/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    result = PaymentController.create_payment(data)
    return jsonify(result)

@plane_bp.route('/api/payments/<int:Payment_ID>/status', methods=['PUT'])
def update_payment_status(Payment_ID):
    status = request.json.get("status")
    result = PaymentController.update_payment_status(Payment_ID, status)
    return jsonify(result)

@plane_bp.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    result = ReviewController.create_review(data)
    return jsonify(result)

@plane_bp.route('/api/reviews/flight/<int:Flight_ID>', methods=['GET'])
def get_reviews_by_flight(Flight_ID):
    result = ReviewController.get_reviews_by_flight(Flight_ID)
    return jsonify(result)

@plane_bp.route('/api/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    result = NotificationController.create_notification(data)
    return jsonify(result)

@plane_bp.route('/api/notifications/passenger/<int:Passenger_ID>', methods=['GET'])
def filter_notifications(Passenger_ID):
    notification_type = request.args.get("notification_type")
    result = NotificationController.filter_notifications(Passenger_ID, notification_type)
    return jsonify(result)

@plane_bp.route('/api/cancellations', methods=['POST'])
def create_cancellation():
    data = request.get_json()
    result = CancellationController.create_cancellation(data)
    return jsonify(result)

@plane_bp.route('/api/cancellations/<int:Booking_ID>/fee', methods=['GET'])
def calculate_cancellation_fee(Booking_ID):
    result = CancellationController.calculate_cancellation_fee(Booking_ID)
    return jsonify(result)

