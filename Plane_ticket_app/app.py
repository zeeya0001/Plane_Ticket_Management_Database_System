
import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from flask_jwt_extended import JWTManager
from Plane_ticket_app.config.config import Config
from Plane_ticket_app.Routes.app_routes import planeticket_bp
from Plane_ticket_app.Routes.user_routes import user_bp
from shared.utils.db_utils import db

app = Flask(__name__)

# Load the configuration before initializing JWTManager or db
app.config.from_object(Config)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Joseph.reso812345@localhost/plane_ticket_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Initialize db and jwt after loading the config
db.init_app(app)
jwt = JWTManager(app)

# Register blueprints after initialization
app.register_blueprint(planeticket_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True, port=4000)