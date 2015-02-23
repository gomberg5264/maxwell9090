from flapy_mail import app
from flapy_mail import mail


def send_email(sender, recipients, subject, body):
    # Send email
    msg = mail.Message()
    msg.sender = sender
    msg.recipients = recipients
    msg.subject = subject
    msg.bcc = ['email1@teste.org', 'email2@teste.org']
    msg.body = body
    with app.app_context():
        mail.send(msg)
