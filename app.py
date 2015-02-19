from flask import Flask, request
from flask.ext.mail import Mail, Message
from flask.ext.sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)


# Models
class Name(db.Model):
    # Include user email in db
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(250), index=True, nullable=True)
    # email = db.Column(db.String(250), index=True, nullable=True)
    # created = db.Column(db.DateTime, default=datetime.utcnow)
    pass


# Views
@app.route('/', methods=['POST'])
def process():
    # Get form POST
    name = request.form["name"]
    email = request.form["email"]
    body_info = ('%s foi cadastrado, email: %s' % (name, email))
    send_email(EMAIL_SENDER, ['email@teste.org'], EMAIL_SUBJECT, body_info)
    # Redirect to success page
    return 'Success!'


def send_email(sender, recipients, subject, body):
    # Send email
    msg = Message()
    msg.sender = sender
    msg.recipients = recipients
    msg.subject = subject
    msg.bcc = ['email1@teste.org', 'email2@teste.org']
    msg.body = body
    with app.app_context():
        mail.send(msg)
