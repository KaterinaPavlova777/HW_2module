from transaction import transaction


def filter_by_currency(currency, transactions=transaction):
    '''
    Принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.
    '''
    for dict_ in transactions:
        if dict_['operationAmount']['currency']['code'] == currency:
            yield dict_


def transaction_descriptions(transactions=transaction):
    '''
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди..
    '''
    for dict_ in transactions:
        yield dict_['description']


def card_number_generator(first, last):
    '''
    Генератор номеров банковских карт, который генерирует номера карт.
    '''
    for card_number in range(first, last + 1):
        result = str(card_number).zfill(16)
        yield f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:]}"
