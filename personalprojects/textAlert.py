import os

from twilio.rest import Client

def send_message_nick(message):

    account_sid = os.environ['ACCOUNT_SID']
    auth_token  = os.environ['AUTH_TOKEN'] 
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        to=os.environ['PHONE'], 
        from_="+12242573437",
        body=message)
    
    print(message.sid)

