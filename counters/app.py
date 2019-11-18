from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from smartcounters import create_app


app = create_app('smartcounters.config.DevelopmentConfig')


if __name__ == '__main__':
    app.run()
