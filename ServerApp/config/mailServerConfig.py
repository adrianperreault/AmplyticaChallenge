#!/usr/bin/env python
"""
Created by: Adrian Perreault (2017)

Description: Mail Server Configuration file. 
   
Requirements: 
   - Set the appropriate settings for your mail server.
   - If using a gmail account, note that 'Allow less Secure apps' setting must 
     be enabled: https://myaccount.google.com/lesssecureapps?pli=1  
             
"""

mailConfig = dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='* CHANGE ME *',
    MAIL_PASSWORD='* CHANGE ME *'
)

