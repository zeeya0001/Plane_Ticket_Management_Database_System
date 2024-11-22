from shared.utils.db_utils import db

class Airport(db.Model):
    __tablename__ = 'airport'
    AP_CODE = db.Column(db.String(10), primary_key=True)
    Airport_name = db.Column(db.String(100), nullable=False)
    Airport_location = db.Column(db.String(50), nullable=False)
    facilities = db.Column(db.String(50), nullable=False)

    
