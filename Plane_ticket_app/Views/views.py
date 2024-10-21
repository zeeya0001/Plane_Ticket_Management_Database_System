from flask import jsonify, request
from Plane_ticket_app.Services.services import (
    PassengerService, FlightService, BookingService,
    AirportServiceService, SeatMatrixService, PaymentService,
    ReviewService, NotificationService, CancellationService
)

def create_passenger():
    data = request.json
    new_passenger = PassengerService.create_passenger(data)
    return jsonify({"message": "Passenger created", "id": new_passenger.Passenger_ID}), 201

def get_all_passengers():
    passengers = PassengerService.get_all_passengers()
    return jsonify([{"id": p.Passenger_ID, "name": f"{p.First_name} {p.Last_name}"} for p in passengers])

def get_flights():
    flights = FlightService.get_all_flights()
    return jsonify([{"id": f.Flight_ID, "name": f.Flight_name} for f in flights])

def create_booking():
    data = request.json
    new_booking = BookingService.create_booking(data)
    return jsonify({"message": "Booking created", "id": new_booking.Booking_ID}), 201

def get_services():
    services = AirportServiceService.get_all_services()
    return jsonify([{"id": s.Service_ID, "name": s.Service_name} for s in services])

def get_seats(flight_id):
    seats = SeatMatrixService.get_seats_for_flight(flight_id)
    return jsonify([{"id": s.Seat_ID, "number": s.Seat_Number, "class": s.Class, "availability": s.Availability} for s in seats])

def create_payment():
    data = request.json
    new_payment = PaymentService.create_payment(data)
    return jsonify({"message": "Payment processed", "id": new_payment.Payment_ID}), 201

def create_review():
    data = request.json
    new_review = ReviewService.create_review(data)
    return jsonify({"message": "Review submitted", "id": new_review.Review_ID}), 201

def create_notification():
    data = request.json
    new_notification = NotificationService.create_notification(data)
    return jsonify({"message": "Notification created", "id": new_notification.Notification_ID}), 201

def create_cancellation():
    data = request.json
    new_cancellation = CancellationService.create_cancellation(data)
    return jsonify({"message": "Cancellation processed", "id": new_cancellation.Cancellation_ID}), 201


