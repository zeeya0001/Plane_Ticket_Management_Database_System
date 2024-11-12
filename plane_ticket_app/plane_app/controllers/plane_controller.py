from flask import request
from plane_app.services.plane_service import (
    PassengerService, FlightService, BookingService,
    AirportServiceService, SeatMatrixService, PaymentService,
    ReviewService, NotificationService, CancellationService
)
from plane_app.views.plane_view import (
    PassengerView, FlightView, BookingView, ServiceView,
    SeatMatrixView, PaymentView, ReviewView, NotificationView,
    CancellationView, PlaneView
)

class PassengerController:
    @staticmethod
    def create_passenger(data):
        passenger = PassengerService.create_passenger(data)
        if passenger:
            return PassengerView.render_passenger(passenger)
        return PlaneView.render_error("Failed to create passenger")
    
    @staticmethod
    def get_all_passengers():
        passengers = PassengerService.get_all_passengers()
        return PassengerView.render_passengers(passengers)
    
    @staticmethod
    def get_passenger_by_id(Passenger_ID):
        passenger = PassengerService.get_passenger_by_id(Passenger_ID)
        if passenger:
            return PassengerView.render_passenger(passenger)
        return PlaneView.render_error("Passenger not found")
    
    @staticmethod
    def update_passenger(Passenger_ID, data):
        passenger = PassengerService.update_passenger(Passenger_ID, data)
        if passenger:
            return PassengerView.render_passenger(passenger)
        return PlaneView.render_error("Failed to update passenger")
    
    @staticmethod
    def delete_passenger(Passenger_ID):
        success = PassengerService.delete_passenger(Passenger_ID)
        if success:
            return PlaneView.render_success("Passenger deleted successfully")
        return PlaneView.render_error("Failed to delete passenger")
    

class FlightController:
    @staticmethod
    def create_flight(data):
        flight = FlightService.create_flight(data)
        if flight:
            return FlightView.render_flight(flight)
        return PlaneView.render_error("Failed to create flight")
    
    @staticmethod
    def get_flight_by_id(Flight_ID):
        flight = FlightService.get_flights_by_id(Flight_ID)
        if flight:
            return FlightView.render_flight(flight)
        return PlaneView.render_error("Flight not found")
    
    @staticmethod
    def get_flights_by_origin_dest(Origin_AP_CODE, Destination_AP_CODE):
        flights = FlightService.get_flights_by_origin_dest(Origin_AP_CODE, Destination_AP_CODE)
        return FlightView.render_flights(flights)
    
    @staticmethod
    def check_availability(Flight_ID):
        available = FlightService.check_availability(Flight_ID)
        return {"availability": available}
    
    @staticmethod
    def get_flights_by_departure_time(Departure_Time):
        flights = FlightService.get_flights_by_departuretime(Departure_Time)
        return FlightView.render_flights(flights)
    
    @staticmethod
    def get_flights_by_arrival_time(Arrival_Time):
        flights = FlightService.get_flights_by_arrivaltime(Arrival_Time)
        return FlightView.render_flights(flights)
    
    @staticmethod
    def update_flight(Flight_ID, data):
        flight = FlightService.update_flight(Flight_ID, data)
        if flight:
            return FlightView.render_flight(flight)
        return PlaneView.render_error("Failed to update Flight")
    
    @staticmethod
    def delete_flight(Flight_ID):
        success = FlightService.delete_flight(Flight_ID)
        if success:
            return PlaneView.render_success("Flight deleted successfully")
        return PlaneView.render_error("Failed to delete flight")
    

class BookingController:
    @staticmethod
    def create_booking(data):
        booking = BookingService.create_booking(data)
        if booking:
            return BookingView.render_booking(booking)
        return PlaneView.render_error("Failed to create booking")
    
    @staticmethod
    def get_bookings_by_passenger(Passenger_ID):
        bookings = BookingService.get_bookings_by_passenger(Passenger_ID)
        return BookingView.render_bookings(bookings)
    
    @staticmethod
    def update_booking_status(Booking_ID, status):
        booking = BookingService.update_booking_status(Booking_ID, status)
        if booking:
            return BookingView.render_booking(booking)
        return PlaneView.render_error("Failed to update booking status")
    
    @staticmethod
    def cancel_booking(Booking_ID):
        cancellation = BookingService.cancel_booking(Booking_ID)
        if cancellation:
            return CancellationView.render_cancellation(cancellation)
        return PlaneView.render_error("Failed to cancel booking")
    

class ServiceController:
    @staticmethod
    def add_service(data):
        service = AirportServiceService.add_service(data)
        if service:
            return ServiceView.render_service(service)
        return PlaneView.render_error("Failed to add service")
    
    @staticmethod
    def get_all_services():
        services = AirportServiceService.get_all_services()
        return ServiceView.render_services(services)
    
    @staticmethod
    def update_service(Service_ID, data):
        service = AirportServiceService.update_service(Service_ID, data)
        if service:
            return ServiceView.render_service(service)
        return PlaneView.render_error("Failed to update service")
    
    @staticmethod
    def delete_service(Service_ID):
        success = AirportServiceService.delete_service(Service_ID)
        if success:
            return PlaneView.render_success("Service deleted successfully")
        return PlaneView.render_error("Failed to delete service")
    

class SeatMatrixController:
    @staticmethod
    def get_seats_for_flight(Flight_ID):
        seats = SeatMatrixService.get_seats_for_flight(Flight_ID)
        return SeatMatrixView.render_seats(seats)
    
    @staticmethod
    def mark_seat_as_booked(Seat_ID):
        seat = SeatMatrixService.mark_seat_as_booked(Seat_ID)
        if seat:
            return SeatMatrixView.render_seat(seat)
        return PlaneView.render_error("Failed to mark seat as booked")
    
    @staticmethod
    def release_seat(Seat_ID):
        seat = SeatMatrixService.release_seat(Seat_ID)
        if seat:
            return SeatMatrixView.render_seat(seat)
        return PlaneView.render_error("Failed to release seat")
    

class PaymentController:
    @staticmethod
    def create_payment(data):
        payment = PaymentService.create_payment(data)
        if payment:
            return PaymentView.render_payment(payment)
        return PlaneView.render_error("Failed to process payment")
    
    @staticmethod
    def update_payment_status(Payment_ID, status):
        payment = PaymentService.update_payment_status(Payment_ID, status)
        if payment:
            return PaymentView.render_payment(payment)
        return PlaneView.render_error("Failed to update payment status")
    

class ReviewController:
    @staticmethod
    def create_review(data):
        review = ReviewService.create_review(data)
        if review:
            return ReviewView.render_review(review)
        return PlaneView.render_error("Failed to create review")
    
    @staticmethod
    def get_reviews_by_flight(Flight_ID):
        reviews = ReviewService.get_reviews_by_flight(Flight_ID)
        return ReviewView.render_reviews(reviews)
    

class NotificationController:
    @staticmethod
    def create_notification(data):
        notification = NotificationService.create_notification(notification)
        if notification:
            return NotificationView.render_notification(notification)
        return PlaneView.render_error("Failed to created notification")
    
    @staticmethod
    def filter_notifications(Passenger_ID, Notification_Type=None):
        notifications = NotificationService.filter_notifications(Passenger_ID, Notification_Type)
        return NotificationView.render_notifications(notifications)


class CancellationController:
    @staticmethod
    def create_cancellation(data):
        cancellation = CancellationService.create_cancellation(data)
        if cancellation:
            return CancellationView.render_cancellation(cancellation)
        return PlaneView.render_error("Failed to process cancellation")

    @staticmethod
    def calculate_cancellation_fee(Booking_ID):
        fee = CancellationService.calculate_cancellation_fee(Booking_ID)
        if fee is not None:
            return {"Cancellation_fee": fee}
        return PlaneView.render_error("Failed to calculate cancellation fee")
