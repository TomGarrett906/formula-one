from flask_smorest import Blueprint

bp = Blueprint("teams", __name__, url_prefix="/team")

from . import routes 