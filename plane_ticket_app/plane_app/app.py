import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from plane_app.routes.plane_routes import plane_bp
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:SW%2318tr%40it%2325@localhost/plane_ticket_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(plane_bp)

@app.route('/')
def home():
    return "Plane app chal rha hai"

if __name__ == '__main__':
    app.run(debug=True, port=4002)