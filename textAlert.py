from twilio.rest import Client
import os
from sys import argv


def messageMe(textMessage="Hello, Nick"):

    account_sid = os.environ.get('ACCOUNT_SID') 
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            from_ = '+12242573437',
            body = textMessage,
            to = os.environ.get('NICK_PHONE')
            )


def main():

    try:
      messageMe(' '.join(argv[1:]))

    except IndexError:
      messageMe()


if __name__ == '__main__':
    main()
