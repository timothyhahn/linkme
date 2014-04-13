from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import settings
import os

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_PATH
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config['DEBUG'] = settings.DEBUG

db = SQLAlchemy(app)

import routes
