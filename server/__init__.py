# import necessary modules
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# initialize flask app
app = Flask(__name__)
app.config.from_object(Config)

# set up database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import routes to avoid circular imports
from . import routes