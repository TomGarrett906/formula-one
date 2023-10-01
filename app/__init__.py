from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from resources.drivers import bp as driver_bp
api.register_blueprint(driver_bp)
from resources.teams import bp as team_bp
api.register_blueprint(team_bp)
from resources.owners import bp as owner_bp
api.register_blueprint(owner_bp)

from resources.drivers import routes
from resources.teams import routes
from resources.owners import routes

from resources.drivers.DriverModel import DriverModel
from resources.teams.TeamModel import TeamModel
from resources.owners.OwnerModel import OwnerModel