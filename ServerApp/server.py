"""
Created by: Adrian Perreault (2017)

Description: A simple web server utilizing the Python microframework Flask to manage a simple web application for
             collecting end-user feedback from a web form and forwarding it to a specified email address. 

Requirements: - This program requires the Flask module: https://pypi.python.org/pypi/Flask/0.12
              - This script requires Python 3.5 or later.
"""
from flask import Flask

app = Flask(__name__)


# This is the entry point route for the web server. The annotation specifies the routing path used when the user
# accesses the site. Ex. User running locally enters http://localhost:5000/ and sees "Hello Amplytica" in their browser.
@app.route("/")
def main():
    return "Hello Amplytica!"


if __name__ == "__main__":
    app.run()
