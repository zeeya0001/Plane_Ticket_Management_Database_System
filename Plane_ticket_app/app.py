
import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from Plane_ticket_app.Routes.App_routes import planeticket_bp
from shared.utils.db_utils import db
import CORS

app = Flask(__name__)
CORS(app)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Joseph.reso812345@localhost/plane_ticket_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(planeticket_bp)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)

