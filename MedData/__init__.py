from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'None'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9766194467manU@localhost/pythonproject'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import views to register routes
    from views import app as views_blueprint
    app.register_blueprint(views_blueprint)

    return app
