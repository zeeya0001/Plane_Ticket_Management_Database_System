from flask import render_template,request,redirect,url_for
from Plane_ticket_app.Services.review_service import ReviewService
from Plane_ticket_app.templates.passenger_views import PassengerView

class ReviewController:
    @staticmethod
    def get_review_by_Review_ID():
        Review_ID = request.form.get('Review_ID')
        review = ReviewService.get_review_by_Review_ID(Review_ID)
        if not review:
            return render_template('render.html', message='review not found'), 404
        return render_template('render.html', message=PassengerView.render_review(review)), 200

    @staticmethod
    def create_review():
        Passenger_ID = request.form.get('Passenger_ID')
        Rating = request.form.get('Rating')
        Content = request.form.get('Content')

        review = ReviewService.create_review(Passenger_ID, Rating, Content)
        if not review.Passenger_ID:
            return render_template('render.html', message='passenger not found'), 404
        return render_template('render.html', message='review created successfully'), 201

    @staticmethod
    def delete_review(Review_ID):
        Review_ID = request.form.get('Review_ID')

        delete_review = ReviewService.delete_review(Review_ID)
        if delete_review:
            return render_template('render.html', message='Review deleted successfully'), 200
        return render_template('render.html', message='Review not found'), 400
    
    @staticmethod
    def create_notification():
        Passenger_ID = request.form.get('Passenger_ID')
        message = request.form.get('message')
        status = request.form.get('status')
        notification_type = "text"
        
        result = ReviewService.create_notification(Passenger_ID, message, status, notification_type)
        if not result.Passenger_ID:
            return render_template('render.html', message='passenger not found'), 404
        return render_template('render.html', message='notification sent successfully'), 201

    @staticmethod
    def get_notifications():
        Passenger_ID = request.form.get('Passenger_ID')
        notification = ReviewService.get_notifications(Passenger_ID)
        if not notification:
            return render_template('render.html', message='notification not found'), 404
        return render_template('get_notification.html', notification=notification), 200

    @staticmethod
    def mark_as_read(Notification_ID):
        status = ReviewService.mark_as_read(Notification_ID)
        return render_template('render.html', message=PassengerView.render_notification(status)), 200

