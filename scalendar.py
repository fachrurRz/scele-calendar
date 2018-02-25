from datetime import datetime
from datetime import timedelta
import settings
import icalendar
from utils import format_datetime


def get_scele_events(calendar_data):
    events = []
    gcal = icalendar.Calendar.from_ical(calendar_data)
    for component in gcal.walk():
        if component.name == "VEVENT":
            summary = component.get('summary')
            categories = component.get('categories')
            description = component.get(
                'description').encode('ascii', 'ignore')
            location = component.get('location')
            startdt = component.get('dtstart').dt
            enddt = component.get('dtend').dt
            start_time = format_datetime(startdt)
            end_time = format_datetime(enddt)

            trello_time_zone = enddt - timedelta(hours=5)
            trello_time = format_datetime(trello_time_zone)

            event_name = '[{}] {}'.format(categories, summary)

            event = {
                'name': event_name,
                'description': description,
                'location': location,
                'start_time': start_time,
                'end_time': end_time,
                'trello_time': trello_time
            }

            events.append(event)

    return events


def get_scele_calendar_data(session):
    r = session.get(settings.CALENDAR_URL)
    calendar_data = r.content
    return calendar_data
