def mask_card_number(card_number):
    return '{} {}** **** {}'.format(card_number[:6], card_number[-4:])


def mask_account_number(account_number):
    return '{}XXXX'.format(account_number[-4:])