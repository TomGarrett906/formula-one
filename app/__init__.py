from flask import Flask

app = Flask(__name__)

from resources.drivers import routes
from resources.teams import routes