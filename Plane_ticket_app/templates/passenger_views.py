class PassengerView:
    @staticmethod
    def render_passenger(passenger):
        return {
            "Passenger_ID": passenger.Passenger_ID,
            "First_name": passenger.First_name,
            "Last_name": passenger.Last_name,
            "age": passenger.age,
            "disabilities": passenger.disabilities,
            "Email": passenger.Email,
            "Passport_number": passenger.Passport_number,
            "Mobile_Number": passenger.Mobile_Number,
            "created_at": passenger.created_at.isoformat()
        }

    @staticmethod
    def render_passengers(passengers):
        return [PassengerView.render_passenger(passenger) for passenger in passengers]


    @staticmethod
    def render_flight(flight):
        return {
            "Flight_name": flight.Flight_name,
            "Arrival_Time": flight.Arrival_Time.isoformat(),
            "Departure_Time": flight.Departure_Time.isoformat(),
            "Year_of_Services": flight.Year_of_Services,
            "Airline_name": flight.Airline_name,
            "Origin_AP_name": flight.Origin_AP_name,
            "Destination_AP_name": flight.Destination_AP_name,
            "Flight_type": flight.Flight_type,
            "total_seats_available": flight.total_seats_available,
            "Class": flight.Class,
            "Flight_Status": flight.Flight_Status,
            "Flight_Location": flight.Flight_Location    
        }

    @staticmethod
    def render_flights(flights):
        return [PassengerView.render_flight(flight) for flight in flights]

    @staticmethod
    def render_booking(booking):
        return {
            "Flight_ID": booking.Flight_ID,
            "Passenger_ID": booking.Passenger_ID,
            "Origin_AP_name": booking.Origin_AP_name,
            "Destination_AP_name": booking.Destination_AP_name,
            "Journey_date": booking.Journey_date.isoformat(),
            "Gender": booking.Gender,
            "Age": booking.Age,
            "Seat_number": booking.Seat_number,
            "Boarding_time": booking.Boarding_time,
            "Check_in_time": booking.Check_in_time,
            "Class": booking.Class,
            "Price": booking.Price,
            "Status": booking.status,
            "created_at": booking.created_at.isoformat()
        }

    @staticmethod
    def render_bookings(bookings):
        return [PassengerView.render_booking(booking) for booking in bookings]

    @staticmethod
    def render_cancel_booking(cancellation):
        return {
            "Booking_ID": cancellation.Booking_ID,
            "Request_time": cancellation.Request_time.isoformat(),
            "Issue_time": cancellation.Issue_time.isoformat(),
            "Amount_refunded": cancellation.Amount_refunded,
            "Reason": cancellation.Reason
        }

    @staticmethod
    def render_cancel_bookings(cancellations):
        return [PassengerView.render_booking(booking) for booking in bookings]

    @staticmethod
    def render_review(review):
        return {
            "Passenger_ID": review.Passenger_ID,
            "Content": review.Content,
            "Rating": review.Rating,
            "Date": review.Date.isoformat()
        }

    @staticmethod
    def render_reviews(reviews):
        return [PassengerView.render_review(review) for review in reviews]


    @staticmethod
    def render_service(service):
        return {
            "Service_name": service.Service_name,
            "about_service": service.about_service,
            "Airport_ID": service.Airport_ID,
            "Booking_ID": service.Booking_ID
        }

    @staticmethod
    def render_services(services):
        return [PassengerView.render_service(service) for service in services]

    @staticmethod
    def render_notification(notification):
        return {
            "Passenger_ID": notification.Passenger_ID,
            "message": notification.message,
            "status": notification.status,
            "notification_type": notification.notification_type,
            "created_at": notification.created_at
        }

    @staticmethod
    def render_notifications(notifications):
        return [PassengerView.render_notification(notification) for notification in notifications]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, Passenger_ID=None, Flight_ID=None, Booking_ID=None, Review_ID=None):
        response = {"message": message}
        if Passenger_ID:
            response["Passenger_ID"] = Passenger_ID
        if Flight_ID:
            response["Flight_ID"] = Flight_ID
        if Booking_ID:
            response["Booking_ID"] = Booking_ID
        if Review_ID:
            response["Review_ID"] = Review_ID
        return response

