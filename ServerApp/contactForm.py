#!/usr/bin/env python
"""
Created by: Adrian Perreault (2017)

Description: A contact us form utilizing Flask-WTF. The data on the form includes:
              - Name         (Required)
              - Email        (Required)
              - Phone Number
              - Subject      (Required)
              - Message      (Required)

Requirements: - This class requires the Flask-WTF module: https://pypi.python.org/pypi/Flask-WTF
              - This script requires Python 3.5 or later.
"""

# Imports:
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators


class ContactUsForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired("Please enter your name.")],
                       render_kw={"placeholder": "Name",
                                  "class": "form-control",
                                  "required": "required"})

    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")],
                        render_kw={"placeholder": "Email",
                                   "class": "form-control",
                                   "type": "email",
                                   "required": "required"}
                        )

    phone = StringField("Phone", render_kw={"placeholder": "Phone",
                                            "class": "form-control"})

    subject = StringField("Subject", [validators.DataRequired("Please enter a subject.")],
                          render_kw={"placeholder": "Subject",
                                     "class": "form-control",
                                     "required": "required"})

    message = TextAreaField("Message", [validators.DataRequired("Please enter a message")],
                            render_kw={"placeholder": "Message",
                                       "class": "form-control",
                                       "rows": "7",
                                       "required": "required"})

    submit = SubmitField("Send", render_kw={"class": "btn btn-primary pull-right"})
