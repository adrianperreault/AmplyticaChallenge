# Amplytica Challenge 


This is a Python web application utilizing Flask for forwarding web form data to a specified email address. 


## Build Instructions: 


### 1. Clone the project:
```
git clone https://github.com/aperreaultTRU/AmplyticaChallenge.git
```

### 2. Install dependencies (Optional if they are installed already): 
```
pip install Flask
pip install Flask-Mail
pip install Flask-WTF
```
### 3. Configure email recipients list:
Open **ServerApp/config/mailServerConfig.py** and add the address/es where you'd like the form data sent.  

```
# A list of email address strings for where the form data should be sent.
EMAIL_RECIPIENTS = ["example@mail.com", "another@mail.com]
```

### 4. Configure email server details:
Still inside **ServerApp/config/mailServerConfig.py**, enter your email server configuration details.

*Gmail Account:* 

**Note 'Allow less Secure apps' setting must be enabled.
     See: https://myaccount.google.com/lesssecureapps?pli=1*
```
mailConfig = dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='** CHANGE ME **',
    MAIL_PASSWORD='** CHANGE ME **'
)
```
*Other Email Servers:* 
```
mailConfig = dict(
    DEBUG=True,
    MAIL_SERVER='** CHANGE ME **',
    MAIL_PORT='** CHANGE ME **,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='** CHANGE ME **',
    MAIL_PASSWORD='** CHANGE ME **'
)
```

### 5. Run the server:
```
cd AmplyticaChallenge/ServerApp
python server.py
```

### 6. Open http://localhost:5000
