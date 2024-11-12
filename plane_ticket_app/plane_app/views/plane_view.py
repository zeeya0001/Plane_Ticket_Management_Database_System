class LocationView:
    @staticmethod
    def render_location(location):
        return {
            "location_id": location.location_id,
            "location_name": location.location_name,
            "city": location.city,
            "address": location.address,
            "country": location.country,
        }

    @staticmethod
    def render_locations(locations):
        return [LocationView.render_location(location) for location in locations]

class PassengerView:
    @staticmethod
    def render_passenger(passenger):
        return {
            "passenger_id": passenger.Passenger_ID,
            "first_name": passenger.First_name,
            "last_name": passenger.Last_name,
            "email": passenger.Email,
            "passport_number": passenger.Passport_number,
            "age": passenger.Age,
            "disabilities": passenger.disabilities,
            "contact_number": passenger.Contact_number,
            "created_at": passenger.created_at,
            "updated_at": passenger.updated_at,
        }
    
    @staticmethod
    def render_passengers(passengers):
        return [PassengerView.render_passenger(passenger) for passenger in passengers]

class AirlineView:
    @staticmethod
    def render_airline(airline):
        return {
            "airline_id": airline.Airline_ID,
            "airline_name": airline.Airline_name,
            "operating_region": airline.Operating_Region,
            "contact_number": airline.Contact_Number,
        }

    @staticmethod
    def render_airlines(airlines):
        return [AirlineView.render_airline(airline) for airline in airlines]


class AirportView:
    @staticmethod
    def render_airport(airport):
        return {
            "ap_code": airport.AP_CODE,
            "Airpot_name": airport.Airpot_name,
            "location_id": airport.location_id,
            "facilities": airport.facilities,
        }

    @staticmethod
    def render_airports(airports):
        return [AirportView.render_airport(airport) for airport in airports]

class FlightView:
    @staticmethod
    def render_flight(flight):
        return {
            "flight_id": flight.Flight_ID,
            "flight_name": flight.Flight_name,
            "departure_time": flight.Departure_Time,
            "arrival_time": flight.Arrival_Time,
            "year_of_services": flight.Year_of_Services,
            "airline_id": flight.Airline_ID,
            "origin_ap_code": flight.Origin_AP_CODE,
            "destination_ap_code":flight.Destination_AP_CODE,
            "flight_type": flight.Flight_Type,
            "flight_status": flight.Flight_Status,
            "created_at": flight.created_at,
            "updated_at": flight.updated_at,
        }
    
    @staticmethod
    def render_flights(flights):
        return [FlightView.render_flight(flight) for flight in flights]
    
class BookingView:
    @staticmethod
    def render_booking(booking):
        return {
            "booking_id": booking.Booking_ID,
            "date": booking.Date,
            "boarding_time": booking.Boarding_time,
            "check_in_time": booking.Check_in_time,
            "price": booking.Price,
            "passnger_id": booking.Passenger_ID,
            "flight_id": booking.Flight_ID,
            "booking_status": booking.Booking_Status,
            "booking_type": booking.Booking_Type,
        }
    
    @staticmethod
    def render_bookings(bookings):
        return [BookingView.render_booking(booking) for booking in bookings]
    
class ServiceView:
    @staticmethod
    def render_service(service):
        return {
            "service_id": service.Service_ID,
            "service_name": service.Service_name,
            "airpot_id": service.Airpot_ID,
            "created_at": service.created_at,
            "updated_at": service.updated_at,
        }
    
    @staticmethod
    def render_services(services):
        return [ServiceView.render_service(service) for service in services]
    
class SeatMatrixView:
    @staticmethod
    def render_seat(seat):
        return {
            "seat_id": seat.Seat_ID,
            "flight_id": seat.Flight_ID,
            "availability": seat.Availability,
            "seat_number": seat.Seat_Number,
            "class": seat.Class,
        }
    
    def render_seats(seats):
        return [SeatMatrixView.render_seat(seat) for seat in seats]
    
class PaymentView:
    @staticmethod
    def render_payment(payment):
        return {
            "payment_id": payment.Payment_ID,
            "amount": payment.Amount,
            "payment_method": payment.Payment_Method,
            "date": payment.Date,
            "payment_status": payment.Payment_Status,
            "booking_id": payment.Booking_ID,
        }
    
    @staticmethod
    def render_payments(payments):
        return [PaymentView.render_payment(payment) for payment in payments]
    
class ReviewView:
    @staticmethod
    def render_review(review):
        return {
            "review_id": review.Review_ID,
            "flight_id": review.Flight_ID,
            "service_id": review.Service_ID,
            "rating": review.Rating,
            "date": review.Date,
            "comment": review.Comment,
            "passenger_id": review.Passenger_ID,
        }

    @staticmethod
    def render_reviews(reviews):
        return [ReviewView.render_review(review) for review in reviews]

class NotificationView:
    @staticmethod
    def render_notification(notification):
        return {
            "notification_id": notification.Notification_ID,
            "passenger_id": notification.Passenger_ID,
            "message": notification.Message,
            "date": notification.Date,
            "notification_type": notification.Notification_Type,
        }

    @staticmethod
    def render_notifications(notifications):
        return [NotificationView.render_notification(notification) for notification in notifications]

class CancellationView:
    @staticmethod
    def render_cancellation(cancellation):
        return {
            "cancellation_id": cancellation.Cancellation_ID,
            "booking_id": cancellation.Booking_ID,
            "request_time": cancellation.Request_time,
            "issue_time": cancellation.Issue_time,
            "reason": cancellation.Reason,
        }

    @staticmethod
    def render_cancellations(cancellations):
        return [CancellationView.render_cancellation(cancellation) for cancellation in cancellations]

class PlaneView:
    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, **kwargs):
        response = {"message": message}
        response.update(kwargs)
        return response