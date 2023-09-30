from flask_smorest import Blueprint

bp = Blueprint("drivers", __name__, url_prefix="/driver", description="Ops on Drivers")

from . import routes 