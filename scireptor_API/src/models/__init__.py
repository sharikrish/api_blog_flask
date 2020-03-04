from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .instance.config import Config
from flask_marshmallow import Marshmallow
# initialize our db
db = SQLAlchemy()
ma = Marshmallow()
def create_app():
        # app initiliazation
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config) #get the configuration file
    db.init_app(app)  # initiating database
    with app.app_context():
        from . import routes
        return app
