from shared.models.review_model import Review
from shared.models.notification_model import Notification
from shared.utils.db_utils import db

class ReviewService:
    @staticmethod
    def create_review(Passenger_ID, Rating, Content):
        new_review = Review(Passenger_ID=Passenger_ID, Rating=Rating, Content=Content)
        db.session.add(new_review)
        db.session.commit()
        return new_review

    @staticmethod
    def get_review_by_id(Review_ID):
        return Review.query.filter_by(Review_ID)

    @staticmethod
    def get_all_reviews():
        return Review.query.all()

    @staticmethod
    def delete_review(Review_ID):
        review = Review.query.filter_by(Review_ID)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False

    @staticmethod
    def create_notification(Passenger_ID, message, status, notification_type):
        
        notification = Notification(Passenger_ID=Passenger_ID, message=message, status=status, notification_type=notification_type
        )
        db.session.add(notification)
        db.session.commit()
        return notification

    @staticmethod
    def get_notifications(Passenger_ID, status=None):
        query = Notification.query.filter_by(Passenger_ID=Passenger_ID)
        if status:
            query = query.filter_by(status=status)
        return query.order_by(Notification.created_at.desc()).all()

    @staticmethod
    def mark_as_read(Notification_ID):
        notification = Notification.query.get(Notification_ID)
        if notification:
            notification.status = "read"
            db.session.commit()
            return {"message": "Notification marked as read", "status": 200}
        return {"message": "Notification not found", "status": 404}