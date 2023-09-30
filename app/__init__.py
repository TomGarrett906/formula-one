from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api
from flask_migrate import Migrate

from Config import Config
from resources.drivers.DriverModel import DriverModel

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migate = Migrate(app)
api = Api(app)

from resources.drivers import bp as driver_bp
api.register_blueprint(driver_bp)
from resources.teams import bp as team_bp
api.register_blueprint(team_bp)

from resources.drivers import routes
from resources.teams import routes