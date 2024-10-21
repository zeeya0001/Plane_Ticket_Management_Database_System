from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from utils.db_utils import db
from Routes.routes import planeticket_bp
import sys, os
sys.path.append(os.getcwd())


print("Current working directory:", os.getcwd())
print("Contents of current directory:", os.listdir())


app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost//plane_ticket_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Initialize SQLAlchemy with the app
# db.init_app(app)


# Register the routes Blueprint
# app.register_blueprint(planeticket_bp)

# Create the database tables
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port = 4000)

