from shared.models.passenger_model import Passenger
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash

class PassengerService:
    @staticmethod
    def create_passenger(Email, password, First_name, Last_name, Passport_number, age, disabilities, Mobile_Number):
        hashed_password = generate_password_hash(password)
        new_passenger = Passenger(Email=Email, password_hash=hashed_password, First_name=First_name, Last_name=Last_name, Passport_number=Passport_number, age=age, disabilities=disabilities, Mobile_Number=Mobile_Number)
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
    