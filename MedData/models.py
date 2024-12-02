from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Primary key
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(225), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    blood_type = db.Column(db.String(3), nullable=False)
    medical_condition = db.Column(db.String(100), nullable=False)
    date_of_admission = db.Column(db.Date, nullable=False)
    doctor = db.Column(db.String(100), nullable=False)
    hospital = db.Column(db.String(100), nullable=False)
    insurance_provider = db.Column(db.String(100), nullable=False)
    billing_amount = db.Column(db.Float, nullable=False)
    admission_type = db.Column(db.String(50), nullable=False)
    discharge_date = db.Column(db.Date, nullable=True)
    medication = db.Column(db.String(100), nullable=False)
    test_results = db.Column(db.String(100), nullable=False)
