from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from counters import create_app


app = create_app('counters.config.DevelopmentConfig')


if __name__ == '__main__':
    app.run()
