from shared.models.passenger_model import Passenger
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash

class PassengerService:
    @staticmethod
    def create_passenger(First_name, Last_name, Passport_number, age, gender, disabilities, Mobile_Number, Seat_number):
        new_passenger = Passenger(First_name=First_name, Last_name=Last_name, Passport_number=Passport_number, age=age, gender=gender, disabilities=disabilities, Mobile_Number=Mobile_Number,seat_number=Seat_number)
        db.session.add(new_passenger)
        db.session.commit()

        return new_passenger

    @staticmethod
    def get_passenger_by_Passenger_ID(Passenger_ID):
        return Passenger.query.filter_by(Passenger_ID=Passenger_ID).first()

    @staticmethod
    def get_all_passengers():
        return Passenger.query.all()

    @staticmethod
    def verify_passenger(Email, password):
        passenger = Passenger.query.filter_by(Email = Email).first()
        if passenger and check_password_hash(passenger.password_hash, password):
            return passenger
        return None

    @staticmethod
    def delete_passenger(Passenger_ID):
        passenger = Passenger.query.get(Passenger_ID)
        if passenger:
            db.session.delete(passenger)
            db.session.commit()
            return True
        return False
    