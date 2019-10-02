import requests
import re
from pprint import pprint


genbook_endpoint = 'https://www.genbook.com/bookings/api/serviceproviders/30230662/services/989056738/resources/989056742?&day=20191130L&view=day'

genbook_response = requests.get(genbook_endpoint)

if genbook_response.status_code != 200:
    raise ApiError('Error, Was unable to get data from genbook: {}'.format(genbook_response.status_code))


pprint(genbook_response.json()['times'])


