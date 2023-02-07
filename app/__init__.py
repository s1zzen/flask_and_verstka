from flask import Flask
from config import Config

from flask_assets import Environment, Bundle

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

assets = Environment(app)
scss = Bundle('main.scss', filters='pyscss', output='assets/all.css')
assets.register('scss_all', scss)

from app import routes, models, forms
