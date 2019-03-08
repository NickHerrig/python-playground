from twilio.rest import Client
import os


def messageMe(textMessage):

    account_sid = os.environ.get('ACCOUNT_SID') 
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            from_ = '+12242573437',
            body = textMessage,
            to = os.environ.get('NICK_PHONE')
            )


def main():

    messageMe("Hello, Nick... How are you today?")

if __name__ == '__main__':
    main()
