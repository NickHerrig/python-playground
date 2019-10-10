import os
import smtplib
import ssl



def send_email(send_to, subject, message):
    """Send an email from nickherrigdeveloper@gmail.com.

    Keyword arguments:
    send_to -- the receiver
    subject -- the subject line
    message -- the contents

    """
    sender_email = "nickherrigdeveloper@gmail.com"

    email = 'Subject: {}\n\n{}'.format(subject, message)
    port = 465
    password = os.environ['DEV_EMAIL_PASS']
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to, email)
