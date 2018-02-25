import requests
import json
from settings import (
    TRELLO_API_URL,

    TRELLO_BOARD_ID,
    TRELLO_LABEL_ID,
    TRELLO_LIST_ID,
    TRELLO_MEMBER_ID
)

from utils import (
    url_builder
)


POST_CARDS_URL = '{}{}'.format(TRELLO_API_URL, '/1/cards')
GET_CARDS_URL = '{}{}{}{}'.format(
    TRELLO_API_URL, '/1/boards/', TRELLO_BOARD_ID, '/cards')


def get_all_cards():
    get_cards_url = url_builder(GET_CARDS_URL)

    response = requests.request("GET", get_cards_url)

    return json.loads(response.text)


def post_new_cards(new_cards):
    post_cards_url = url_builder(POST_CARDS_URL)
    for new_card in new_cards:
        requests.post(post_cards_url, params=new_card)


def get_trello_card_names(cards):
    card_names = []
    for card in cards:
        card_names.append(card['name'])

    return card_names


def get_new_trello_cards(current_cards, new_events):
    result_events = [
        event for event in new_events if event['name'] not in current_cards]

    new_cards = []

    for event in result_events:
        new_card = {
            'name': event['name'],
            'desc': event['description'],
            'pos': 'top',
            'due': event['trello_time'],
            'idList': TRELLO_LIST_ID,
            'idMember': TRELLO_MEMBER_ID,
            'idLabels': TRELLO_LABEL_ID,
            'keepFromSource': 'all'
        }

        new_cards.append(new_card)

    return new_cards
