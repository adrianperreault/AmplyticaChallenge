#!/usr/bin/env python
"""
Created by: Adrian Perreault (2017)

Description: A simple web server utilizing the Python microframework Flask to manage a simple web application for
             collecting end-user feedback from a web form and forwarding it to a specified email address. 

Requirements: - This program requires the Flask module: https://pypi.python.org/pypi/Flask/0.12
              - This program requires the Flask-Mail module: https://pypi.python.org/pypi/Flask-Mail
              - This script requires Python 3.5 or later.
"""

# Imports:
from flask import Flask, render_template, request
from flask_mail import Mail, Message

from ServerApp.config.mailServerConfig import mailConfig, EMAIL_RECIPIENTS
from ServerApp.contactForm import ContactUsForm

app = Flask(__name__)

# A secret key is required for Flask-WTF's CSRF protection.
app.secret_key = 'development key'

# We configure Flask-Mail mail server settings with the settings saved in ServerApp/config/mailServerConfig
app.config.update(mailConfig)

mail = Mail(app)


# This is the entry point route for the web server. The annotation specifies the routing path used when the user
# accesses the site. Ex. User running locally enters http://localhost:5000/ and sees "Hello Amplytica" in their browser.
@app.route("/")
def index():
    hasSetRecipient = checkIfSetRecipient()
    hasSetMailConfig = checkIfSetMailConfig()

    return render_template('index.html',
                           hasSetRecipient=hasSetRecipient,
                           hasSetMailConfig=hasSetMailConfig)


# Route for the Contact Us web form page.
@app.route("/contact", methods=['GET', 'POST'])
def contactUs():
    form = ContactUsForm()
    if request.method == 'POST':
        handleFormSubmitted(form)
        return render_template('message_sent_page.html')
    elif request.method == 'GET':
        return render_template('contact_page.html', form=form)


# This method handles a form submission by extracting the form data and sending an email.
def handleFormSubmitted(form):
    data = getDataFromForm(form)
    print(data)
    sendEmail(data)


# This method sends an email containing the form data to the specified email address/es.
def sendEmail(data):
    msg = Message(data['subject'],
                  sender=data['email'],
                  recipients=EMAIL_RECIPIENTS)
    msg.html = render_template('email.html',
                               name=data['name'],
                               email=data['email'],
                               phone=data['phone'],
                               subject=data['subject'],
                               message=data['message'])
    mail.send(msg)


# This method returns a dictionary with data extracted from the submitted form.
def getDataFromForm(form):
    data = {
        'name': form.name._value(),
        'email': form.email._value(),
        'phone': form.phone._value(),
        'subject': form.subject._value(),
        'message': form.message._value()
    }
    return data


# This method checks to see if the email recipient list in config/mailServerConfig.py has been set
def checkIfSetRecipient():
    return True if (EMAIL_RECIPIENTS != ["** CHANGE ME **"]) else False

# This method checks to see if the email config details in config/mailServerConfig.py has been set
def checkIfSetMailConfig():
    return True if (
        mailConfig['MAIL_USERNAME'] != '** CHANGE ME **' and
        mailConfig['MAIL_PASSWORD'] != '** CHANGE ME **') else False


if __name__ == "__main__":
    app.run(debug=True)
