from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate

# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Joseph.reso812345@localhost/plane_ticket_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)

from shared.models import airline_model
from shared.models import airport_model
from shared.models import booking_model
from shared.models import cancellation_model
from shared.models import flight_model
from shared.models import notification_model
from shared.models import passenger_model
from shared.models import payment_model
from shared.models import review_model
from shared.models import seatMatrix_model
from shared.models import service_model

