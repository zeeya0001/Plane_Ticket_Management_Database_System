from flask import request
from Plane_ticket_app.Services.review_service import ReviewService
from Plane_ticket_app.templates.passenger_views import PassengerView

class ReviewController:
    @staticmethod
    def get_review():
        Review_ID = request.form.get('Review_ID')
        review = ReviewService.get_review_by_Review_ID(Review_ID)
        if not review: # if review is None:
            return PassengerView.render_error('review not found'), 404
        return PassengerView.render_review(review), 200

    @staticmethod
    def create_review():
        data = request.form
        Passenger_ID = data.get('Passenger_ID')
        Rating = data.get('Rating')
        Content = data.get('Content')

        review = ReviewService.create_review(Passenger_ID, Rating, Content)
        return PassengerView.render_success('review created successfully', review.Review_ID), 201

    @staticmethod
    def delete_review(Review_ID):
        # data = request.form
        # Review_ID = data.get('Review_ID')

        delete_review = ReviewService.delete_review(Review_ID)
        if delete_review:
            return PassengerView.render_success('Review deleted successfully'), 200
        return PassengerView.render_error('Review not found'), 400
    
    @staticmethod
    def create_notification():
        data = request.form
        Passenger_ID = data.get('Passenger_ID')
        message = data.get('message')
        status = data.get('status')
        notification_type = data.get('notification_type')
        
        result = ReviewService.create_notification(Passenger_ID, message, status, notification_type)
        return PassengerView.render_success('notification created successfully'), 201

    @staticmethod
    def get_notifications():
        Passenger_ID = request.form.get('Passenger_ID')
        notification = ReviewService.get_notifications(Passenger_ID, status)
        if not notification: 
            return PassengerView.render_error('notification not found'), 404
        return PassengerView.render_notification(notification), 200

    @staticmethod
    def mark_as_read(Notification_ID):
        status = ReviewService.mark_as_read(Notification_ID)
        return PassengerView.render_notification(status), 200
        
