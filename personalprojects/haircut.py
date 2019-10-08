from datetime import datetime, timedelta
from pprint import pprint

import requests

barbers_endpoints = {
    'jordan':'https://www.genbook.com/bookings/api/serviceproviders/30230662/services/989056738/resources/989056742?',
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


def format_appointments(appointments):
    return [datetime(int(date[:4]),int(date[4:6]),int(date[6:8])) for date in appointments]


def this_weeks_appointments(available_apointments):
    week_from_today = datetime.today() + timedelta(days=7)
    return [date for date in available_apointments if date < week_from_today]


def main():
    all_appointments = get_available_appointments('kegan')
    appointment_dates = format_appointments(all_appointments)
    current_weeks_appointments = this_weeks_appointments(appointment_dates)

    for appointment in current_weeks_appointments:
        pprint(appointment.strftime('%b/%d/%Y'))

if __name__ == '__main__':
    main()
