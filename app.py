from flask import Flask, request
from celery import Celery
from flask_mail import Mail, Message
import logging
from datetime import datetime

app = Flask(__name__)

# Configure Flask-Mail
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='the.opemi.aa@gmail.com',
    MAIL_PASSWORD='zpct buhr giqw bgla'
)

mail = Mail(app)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_async_email(recipient):
    msg = Message('Hello', sender='your-email@example.com', recipients=[recipient])
    msg.body = 'This is a test email.'
    with app.app_context():
        mail.send(msg)

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')
    
    if sendmail:
        send_async_email.delay(sendmail)
        return f"Email queued for {sendmail}"
    
    if talktome:
        with open('/var/log/messaging_system.log', 'a') as log_file:
            log_file.write(f"{datetime.now()} - Talk to me\n")
        return "Logged current time"
    
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
