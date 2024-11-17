from flask import Blueprint, redirect, url_for, render_template, request
from Plane_ticket_app.Controllers.passenger_controller import PassengerController
from Plane_ticket_app.Controllers.booking_controller import BookingController
from Plane_ticket_app.Controllers.review_controller import ReviewController
from Plane_ticket_app.Controllers.flight_controller import FlightController

planeticket_bp = Blueprint('planeticket_bp', __name__,url_prefix='/api')

# @planeticket_bp.route('/', methods=['GET'])
# def home():
#     return render_template('home.html')

@planeticket_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        return PassengerController.create_passenger()

@planeticket_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return PassengerController.login_passenger()

# Booking Routes
@planeticket_bp.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'GET':
        return render_template('Book_ticket.html')
    elif request.method == 'POST':
        return BookingController.book_ticket()

@planeticket_bp.route('/booking/', methods=['GET'])
def get_booking():
    return BookingController.get_booking()

@planeticket_bp.route('/payment', methods=['POST'])
def process_payment():
    return BookingController.process_payment()

@planeticket_bp.route('/payment/status/<int:Booking_id>', methods=['GET'])
def payment_status(Booking_id):
    return BookingController.get_payment_status(Booking_id)

@planeticket_bp.route('/booking/cancel', methods=['GET', 'POST'])
def cancel_booking():
    if request.method == 'GET':
        return render_template('cancel_booking.html')
    elif request.method == 'POST':
        return BookingController.cancel_booking()

# Flight Routes
@planeticket_bp.route('/flight/', methods=['GET'])
def get_flight():
    return FlightController.get_flight()

@planeticket_bp.route('/flight', methods=['GET', 'POST'])
def create_flight():
    if request.method == 'GET':
        return render_template('create_flight.html')
    elif request.method == 'POST':
        return FlightController.create_flight()

# Passenger Routes
@planeticket_bp.route('/passenger/<int:Passenger_ID>', methods=['GET'])
def get_passenger(Passenger_ID):
    return PassengerController.get_passenger(Passenger_ID)

@planeticket_bp.route('/passenger', methods=['GET', 'POST'])
def create_passenger():
    if request.method == 'GET':
        return render_template('create_passenger.html')
    elif request.method == 'POST':
        return PassengerController.create_passenger()

@planeticket_bp.route('/passenger/login', methods=['POST'])
def login_passenger():
    return PassengerController.login_passenger()

# Review Routes
@planeticket_bp.route('/review/', methods=['GET'])
def get_review():
    return ReviewController.get_review()

@planeticket_bp.route('/review', methods=['GET', 'POST'])
def create_review():
    if request.method == 'GET':
        return render_template('create_review.html')
    elif request.method == 'POST':
        return ReviewController.create_review()

@planeticket_bp.route('/review', methods=['GET', 'DELETE'])
def manage_review():
    if request.method == 'GET':
        return ReviewController.get_review()
    elif request.method == 'DELETE':
        return ReviewController.delete_review()

@planeticket_bp.route('/notification', methods=['GET', 'POST'])
def manage_notification():
    if request.method == 'GET':
        return render_template('get_notification.html')
    elif request.method == 'POST':
        return ReviewController.create_notification()

# Notification Routes
@planeticket_bp.route('/notifications/', methods=['GET'])
def get_notifications():
    return ReviewController.get_notifications()

@planeticket_bp.route('/notifications/<int:Notification_ID>/read', methods=['PATCH'])
def mark_as_read(Notification_ID):
    return ReviewController.mark_as_read(Notification_ID)