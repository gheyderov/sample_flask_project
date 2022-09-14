from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app import app



db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
