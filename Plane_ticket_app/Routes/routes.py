from flask import Blueprint
from Controllers.controller import (
    PassengerController, FlightController, BookingController,
    ServiceController, SeatController, PaymentController,
    ReviewController, NotificationController, CancellationController
)

planeticket_bp = Blueprint('planeticket_bp', __name__)

# Passenger @planeticket_bp
@planeticket_bp.route('/passengers', methods=['POST'])(PassengerController.create_passenger)
@planeticket_bp.route('/passengers', methods=['GET'])(PassengerController.get_all_passengers)

# Flight @planeticket_bp
@planeticket_bp.route('/flights', methods=['GET'])(FlightController.get_flights)

# Booking @planeticket_bp
@planeticket_bp.route('/bookings', methods=['POST'])(BookingController.create_booking)

# Service @planeticket_bp
@planeticket_bp.route('/services', methods=['GET'])(ServiceController.get_services)

# Seat @planeticket_bp
@planeticket_bp.route('/flights/<int:flight_id>/seats', methods=['GET'])(SeatController.get_seats)

# Payment @planeticket_bp
@planeticket_bp.route('/payments', methods=['POST'])(PaymentController.create_payment)

# Review @planeticket_bp
@planeticket_bp.route('/reviews', methods=['POST'])(ReviewController.create_review)

# Notification @planeticket_bp
@planeticket_bp.route('/notifications', methods=['POST'])(NotificationController.create_notification)

# Cancellation @planeticket_bp
@planeticket_bp.route('/cancellations', methods=['POST'])(CancellationController.create_cancellation)
