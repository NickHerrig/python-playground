import requests
from pprint import pprint
import datetime


barbers_dates_open = {
    'jordan':'https://www.genbook.com/bookings/api/serviceproviders/30230662/services/989056738/resources/989056742?',
    'kegan':'https://www.genbook.com/bookings/api/serviceproviders/30352805/services/2098565278/resources/2098565282?',
}


genbook_response = requests.get(barbers_dates_open['kegan'])

if genbook_response.status_code != 200:
    raise ApiError('Error, Was unable to get data from genbook: {}'.format(genbook_response.status_code))
dates = genbook_response.json()['dates']
clean_dates = [ date[:-1] for date in dates]
apointment_dates = [datetime.datetime(int(date[:4]),int(date[4:6]),int(date[6:]))
                    for date in clean_dates]

one_week_from_today = datetime.datetime.now() + datetime.timedelta(days=7) 
