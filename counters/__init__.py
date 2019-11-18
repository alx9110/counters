from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from smartcounters.models import db
from smartcounters.resources import register_resources


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    # Database
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    register_resources(app, '/api')
    return app
