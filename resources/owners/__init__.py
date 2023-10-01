from flask_smorest import Blueprint

bp = Blueprint("owners", __name__, url_prefix="/owner", description="Ops on Owners")

from . import routes