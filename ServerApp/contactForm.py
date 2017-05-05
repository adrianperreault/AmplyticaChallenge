from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators


class ContactUsForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name.")],
                       render_kw={"placeholder": "Name",
                                  "class": "form-control",
                                  "required": "required"})

    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")],
                        render_kw={"placeholder": "Email",
                                   "class": "form-control"})

    phone = StringField("Phone", render_kw={"placeholder": "Phone",
                                            "class": "form-control"})

    subject = StringField("Subject", [validators.DataRequired("Please enter a subject.")],
                          render_kw={"placeholder": "Subject",
                                     "class": "form-control",
                                     "required": "required"})

    message = TextAreaField("Message", [validators.DataRequired("Please enter a message")],
                            render_kw={"placeholder": "Message",
                                       "class": "form-control",
                                       "maxlength": "140",
                                       "rows": "7",
                                       "required": "required"})

    submit = SubmitField("Send", render_kw={"class": "btn btn-primary pull-right"})
