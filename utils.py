from datetime import datetime
from settings import (
    TRELLO_API_KEY,
    TRELLO_TOKEN
)

import icalendar
import json


def format_datetime(datetime):
    return datetime.strftime('%Y-%m-%dT%H:%M:%S')


def url_builder(url):
    return '{}{}{}{}{}'.format(url, '?fields=name,url&key=', TRELLO_API_KEY, '&token=', TRELLO_TOKEN)
