
from __main__ import app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

class trabajador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    weekly_hours = db.Column(db.Integer, nullable=False)
    function = db.Column(db.String(2), nullable=False)  # DO, AD, TE
    location = db.Column(db.String(3), nullable=False)  # D01, D02, D03
    records = db.relationship('AttendanceRecord', backref='worker', lazy=True)