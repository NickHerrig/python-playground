from datetime import datetime, timedelta
from pprint import pprint

import requests

from pymail import send_email

barbers_endpoints = {
    'jordan':'https://www.genbook.com/bookings/api/serviceproviders/30230662/services/989056738/resources/989056742?',
    'pete': 'https://www.genbook.com/bookings/api/serviceproviders/31191440/services/10282291592/resources/10282190294',
    'brandon':'https://www.genbook.com/bookings/api/serviceproviders/30377943/services/2394050193/resources/2394025610',
    'luis':'https://www.genbook.com/bookings/api/serviceproviders/30250062/services/1173749692/resources/1173749696',
    'zach':'https://www.genbook.com/bookings/api/serviceproviders/30302725/services/1547629284/resources/1547629288',
    'pual':'https://www.genbook.com/bookings/api/serviceproviders/30309745/services/1603733980/resources/1603733984',
    'kegan':'https://www.genbook.com/bookings/api/serviceproviders/30352805/services/2098565278/resources/2098565282?',
}


def get_available_appointments(barber):
    try:
        genbook_response = requests.get(barbers_endpoints[barber])
        if genbook_response.status_code != 200:
            print("Unable to reach genbook endpoint")
            raise SystemExit
        return genbook_response.json()['dates']

    except KeyError:
        print("No barber: {} in barber endpoints".format(barber))
        raise SystemExit


def this_weeks_appointments(appointments):
    available_apointments = [datetime(int(date[:4]),int(date[4:6]),int(date[6:8])) for date in appointments]
    week_from_today = datetime.today() + timedelta(days=7)
    return [date.strftime('%b/%d/%Y') for date in available_apointments if date < week_from_today]


def main():
    for barber in barbers_endpoints.keys():
        all_appointments = get_available_appointments(barber)
        last_minute_appointments = this_weeks_appointments(all_appointments)

        if last_minute_appointments:
            print(barber, "has apointments on", last_minute_appointments)
            # send_email("6302349125@txt.att.net", "Hair Jordan has Availability!", pretty_dates)
        else:
            print(barber, "has no availability.")

if __name__ == '__main__':
    main()
