from datetime import datetime


def change_foreign_keys(cards_data, fk_data, fk_id, new_field):
    for card_data in cards_data:
        fk_dict = list(
            filter(lambda fk_dict: fk_dict["id"] == card_data[fk_id], fk_data)
        )[0]
        card_data[fk_id] = fk_dict[new_field]
    return cards_data


def change_multiple_foreign_keys(cards_data, fk_data, fk_id, new_field):
    for card_data in cards_data:
        fk_array = list(
            filter(lambda fk_array: fk_array["id"] in card_data[fk_id], fk_data)
        )
        if len(fk_array) > 0:
            card_data[fk_id] = [fk_dict[new_field] for fk_dict in fk_array]
    return cards_data


def format_date(cards_data, date_field_name):
    for card_data in cards_data:
        if card_data[date_field_name] is not None:
            start_date = datetime.strptime(
                card_data[date_field_name], "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            new_date = start_date.strftime("%d-%m-%Y")
            card_data[date_field_name] = new_date
    return cards_data
