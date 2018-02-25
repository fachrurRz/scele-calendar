from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CALENDAR_ID = os.environ.get("CALENDAR_ID")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

USERNAME = os.environ.get("SSO_USERNAME")
PASSWORD = os.environ.get("PASSWORD")

LOGIN_URL = 'https://scele.cs.ui.ac.id/login/index.php'
CALENDAR_URL = 'https://scele.cs.ui.ac.id/calendar/export_execute.php?userid=1067&authtoken=205c71c7871d3daa6e3fc927d1ede0de6e03a5ce&preset_what=all&preset_time=recentupcoming'


TRELLO_API_URL = 'https://api.trello.com'

TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")
TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

TRELLO_BOARD_ID = os.environ.get("TRELLO_BOARD_ID")
TRELLO_LIST_ID = os.environ.get("TRELLO_LIST_ID")
TRELLO_MEMBER_ID = os.environ.get("TRELLO_MEMBER_ID")
TRELLO_LABEL_ID = os.environ.get("TRELLO_LABEL_ID")
