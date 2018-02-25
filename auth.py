import requests
import settings

payload = {
    'username': settings.USERNAME,
    'password': settings.PASSWORD
}


def session():
    with requests.Session() as s:
        p = s.post(settings.LOGIN_URL, data=payload)
        return s
