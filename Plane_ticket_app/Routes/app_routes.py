from flask import Blueprint, redirect, url_for, render_template,request
from flask_login import login_required, current_user, logout_user, login_user
from flask_jwt_extended import jwt_required, get_jwt_identity
from Plane_ticket_app.middleware.auth_middleware import admin_required
from Plane_ticket_app.Controllers.passenger_controller import PassengerController
from Plane_ticket_app.Controllers.booking_controller import BookingController
from Plane_ticket_app.Controllers.review_controller import ReviewController
from Plane_ticket_app.Controllers.flight_controller import FlightController
from Plane_ticket_app.Controllers.user_controller import UserController


planeticket_bp = Blueprint('planeticket_bp', __name__)

@planeticket_bp.route('/', methods=['GET'])
def start():
    return render_template('home.html')

@planeticket_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        return UserController.register()

@planeticket_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return UserController.login()



@planeticket_bp.route('/ticket/<int:Flight_ID>/<int:no_of_passengers>/<int:p_id>', methods=['GET'])
def ticket(Flight_ID,no_of_passengers,p_id):
    return BookingController.ticket(Flight_ID=Flight_ID, no_of_passengers=no_of_passengers,p_id=p_id)

# Booking Routes
@admin_required
@planeticket_bp.route('/booking/create', methods=['GET', 'POST'])
def create_booking():
    if request.method == 'GET':
        return render_template('Book_ticket.html')
    elif request.method == 'POST':
        return BookingController.book_ticket()

@login_required
@planeticket_bp.route('/booking', methods=['GET', 'POST'])
def get_booking():
    if request.method == 'GET':
        return render_template('get_booking.html')
    elif request.method == 'POST':
        return BookingController.get_booking()

@planeticket_bp.route('/payment/<int:Flight_ID>/<int:no_of_passengers>/<int:p_id>', methods=['GET', 'POST'])
def process_payment(Flight_ID,no_of_passengers,p_id):
    if request.method == 'GET':
        return render_template('payment.html')
    elif request.method == 'POST':
        print(Flight_ID)
        return BookingController.process_payment(Flight_ID,no_of_passengers,p_id)

@planeticket_bp.route('/payment/status/<int:Booking_id>', methods=['GET'])
def payment_status(Booking_id):
    return BookingController.get_payment_status(Booking_id)

@login_required
@planeticket_bp.route('/booking/cancel', methods=['GET', 'POST'])
def cancel_booking():
    if request.method == 'GET':
        return render_template('cancel_booking.html')
    elif request.method == 'POST':
        return BookingController.cancel_booking()

# Flight Routes
@planeticket_bp.route('/flight_nm>', methods=['post'])
def get_flight_by_flight_name():
    Flight_name = request.form.get('flight_name')
    return FlightController.get_flight_by_Flight_name(Flight_name)

@planeticket_bp.route('/flight_id/<int:Flight_ID>', methods=['GET'])
def get_flight_by_id(Flight_ID):
    return FlightController.get_flight_by_id(Flight_ID)

@planeticket_bp.route('/flight/search', methods=['GET','POST'])
def get_flight():
    if request.method == 'GET':
        return render_template('search_flight.html')
    elif request.method == 'POST':
        Origin_AP_name = request.form.get('Origin_AP_name')
        Destination_AP_name = request.form.get('Destination_AP_name')
        Date = request.form.get('Date')
        no_of_passengers = int(request.form.get('no_of_passengers')) if request.form.get('no_of_passengers') else request.form.get('no_of_passengers')

    return FlightController.get_flight_by_Origin_and_Destination_AP_name(Origin_AP_name, Destination_AP_name,Date, no_of_passengers)

@planeticket_bp.route('/passenger_details/<int:Flight_ID>/<int:no_of_passengers>', methods=['GET'])
def passenger_details(Flight_ID, no_of_passengers):
    return render_template('passenger_details.html', no_of_passengers=no_of_passengers, Flight_ID=Flight_ID)

@admin_required
@planeticket_bp.route('/flight', methods=['GET', 'POST'])
def create_flight():
    if request.method == 'GET':
        return render_template('create_flight.html')
    elif request.method == 'POST':
        return FlightController.create_flight()

# Passenger Routes
@admin_required
@planeticket_bp.route('/passenger', methods=['GET', 'POST'])
def get_passenger():
    if request.method == 'GET':
        return render_template('get_passenger.html')
    elif request.method == 'POST':
        Passenger_ID = request.form.get('Passenger_ID')
        return PassengerController.get_passenger(Passenger_ID)

@admin_required
@planeticket_bp.route('/passengers', methods=['GET'])
def get_all_passengers():
    return PassengerController.get_all_passengers()


@planeticket_bp.route('/passenger/create', methods=['GET', 'POST'])
def create_passenger():
    if request.method == 'GET':
        return render_template('create_passenger.html')
    elif request.method == 'POST':
        return PassengerController.create_passenger()

# @planeticket_bp.route('/passenger/login', methods=['POST'])
# def login_passenger():
#     return PassengerController.login_passenger()

# Review Routes
@planeticket_bp.route('/review/', methods=['GET', 'POST'])
def get_review():
    if request.method == 'GET':
        return render_template('get_review.html')
    elif request.method == 'POST':
        return ReviewController.get_review_by_Review_ID()

@login_required
@planeticket_bp.route('/review/create', methods=['GET', 'POST'])
def create_review():
    if request.method == 'GET':
        return render_template('create_review.html')
    elif request.method == 'POST':
        return ReviewController.create_review()

@login_required
@planeticket_bp.route('/review', methods=['GET', 'POST'])
def delete_review():
    if request.method == 'GET':
        return render_template('delete_review.html')
    elif request.method == 'POST':
        Review_ID = request.form.get('Review_ID')
        return ReviewController.delete_review(Review_ID)

# Notification Routes
@admin_required
@planeticket_bp.route('/notification', methods=['GET', 'POST'])
def create_notification():
    if request.method == 'GET':
        return render_template('create_notification.html')
    elif request.method == 'POST':
        return ReviewController.create_notification()

@login_required
@planeticket_bp.route('/notifications/', methods=['GET', 'POST'])
def get_notifications():
    if request.method == 'GET':
        return render_template('get_notification.html')
    elif request.method == 'POST':
        return ReviewController.get_notifications()

@login_required
@planeticket_bp.route('/notifications/<int:Notification_ID>/read', methods=['PATCH'])
def mark_as_read(Notification_ID):
    return ReviewController.mark_as_read(Notification_ID)

@admin_required
@planeticket_bp.route('/service', methods=['POST'])
def create_service():
    return ReviewController.create_service()

# Notification Routes
@planeticket_bp.route('/service/<int:Service_ID>', methods=['GET'])
def get_services(Service_ID):
    return ReviewController.get_services(Service_ID)

@admin_required
@planeticket_bp.route('/service/<int:Service_ID>/update', methods=['PATCH'])
def update_service(Service_ID):
    return ReviewController.update_service(Service_ID)