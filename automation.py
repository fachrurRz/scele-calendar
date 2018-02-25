import auth
import scalendar
import trello


def update_trello():

    session = auth.session()
    raw_calendar_data = scalendar.get_scele_calendar_data(session)
    scele_events = scalendar.get_scele_events(raw_calendar_data)

    trello_cards = trello.get_all_cards()
    trello_card_names = trello.get_trello_card_names(trello_cards)
    trello_new_cards = trello.get_new_trello_cards(
        trello_card_names, scele_events)
    trello.post_new_cards(trello_new_cards)


update_trello()
