import smtplib
import ssl
from getpass import getpass

sender_email = "nickherrigdeveloper@gmail.com"
receiver_email = "neherrig@gmail.com"
message = """\
Subject: Hair Cuts! 

This message is sent from Python."""


port = 465
password = getpass("enter your password: ") 

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("nickherrigdeveloper@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
