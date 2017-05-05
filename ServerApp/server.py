"""
Created by: Adrian Perreault (2017)

Description: A simple web server utilizing the Python microframework Flask to manage a simple web application for
             collecting end-user feedback from a web form and forwarding it to a specified email address. 

Requirements: - This program requires the Flask module: https://pypi.python.org/pypi/Flask/0.12

              - This program requires the Flask-Mail module: https://pypi.python.org/pypi/Flask-Mail
              - This script requires Python 3.5 or later.
"""
from flask import Flask
from flask_mail import Mail
from flask_mail import Message

from ServerApp.Config.mailServerConfig import mailConfig

app = Flask(__name__)

# We configure Flask-Mail mail server settings with the settings saved in ServerApp/Config/mailServerConfig
app.config.update(mailConfig)

mail = Mail(app)


# This is the entry point route for the web server. The annotation specifies the routing path used when the user
# accesses the site. Ex. User running locally enters http://localhost:5000/ and sees "Hello Amplytica" in their browser.
@app.route("/")

def index():
    msg = Message("Test Email!",
                  sender="adrian-perreault@mytru.ca",
                  recipients=["adrian-perreault@mytru.ca"])
    msg.body = "Testing"
    mail.send(msg)

    return "Hello Amplytica!"


if __name__ == "__main__":
    app.run()
