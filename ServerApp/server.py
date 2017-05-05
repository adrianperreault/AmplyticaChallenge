"""
Created by: Adrian Perreault (2017)

Description: A simple web server utilizing the Python microframework Flask to manage a simple web application for
             collecting end-user feedback from a web form and forwarding it to a specified email address. 

Requirements: - This program requires the Flask module: https://pypi.python.org/pypi/Flask/0.12

              - This program requires the Flask-Mail module: https://pypi.python.org/pypi/Flask-Mail
              - This script requires Python 3.5 or later.
"""
from flask import Flask
from flask import render_template
from flask_mail import Mail

from ServerApp.Config.mailServerConfig import mailConfig

app = Flask(__name__)

# We configure Flask-Mail mail server settings with the settings saved in ServerApp/Config/mailServerConfig
app.config.update(mailConfig)

mail = Mail(app)


# This is the entry point route for the web server. The annotation specifies the routing path used when the user
# accesses the site. Ex. User running locally enters http://localhost:5000/ and sees "Hello Amplytica" in their browser.
@app.route("/")
def index():
    return render_template('index.html')


# Route for the Contact Us web form page.
@app.route("/contact")
def contactUs():
    return render_template('contact_page.html')


if __name__ == "__main__":
    app.run()
