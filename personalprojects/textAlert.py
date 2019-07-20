from twilio.rest import Client
import os
import datetime


account_sid = os.environ['ACCOUNT_SID']
auth_token  = os.environ['AUTH_TOKEN'] 
time = datetime.datetime(2020, 7, 5) - datetime.datetime.now()

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=os.environ['PHONE'], 
    from_="+12242573437",
    body=str(time.days) + " days left.")

print(message.sid)

