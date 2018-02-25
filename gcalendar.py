import pycronofy
import settings


def get_calendar_events():
    cronofy = pycronofy.Client(access_token=settings.ACCESS_TOKEN)
    events = cronofy.read_events()

    for event in events:
        print event
