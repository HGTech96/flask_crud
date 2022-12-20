from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from .views import views
from .auth import auth

db = SQLAlchemy()
DB_NAME = "database.db"

from .models import User, Note


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random key we want'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://john:password@localhost/pets'
    db.init_app(app)

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')