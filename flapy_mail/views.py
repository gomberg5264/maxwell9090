from flapy_mail import app
from flask import request
from flapy_mail.process import send_email
from config import EMAIL_SUBJECT, EMAIL_SENDER


@app.route('/', methods=['POST'])
def process():
    # Get form POST
    name = request.form["name"]
    email = request.form["email"]
    body_info = ('%s foi cadastrado, email: %s' % (name, email))
    send_email(EMAIL_SENDER, ['email@teste.org'], EMAIL_SUBJECT, body_info)
    # Redirect to success page
    return 'Success!'
