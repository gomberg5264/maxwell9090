from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)

from flapy_mail import views
