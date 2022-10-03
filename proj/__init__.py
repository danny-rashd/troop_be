from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import proj.config
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)
# load config
config_name = os.getenv('FLASK_CONFIGURATION', 'default')
app.config.from_object(config.config_setting[config_name])  # object-based default configuration
app.config.from_pyfile('flask.cfg', silent=True)  # instance-folders configuration
# ---

# create tables
db = SQLAlchemy(app)
from proj import model

# db.drop_all()
db.create_all()
# ---

# initiate and register blueprints
# from proj.views.api import bp_api
# app.register_blueprint(bp_api, url_prefix='/api')

# ---
