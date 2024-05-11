from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from transaction import transaction


def test_filter_by_currency() -> None:
    result = list(filter_by_currency("USD", transaction))
    assert len(result) == 3
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == "USD"


def test_transaction_descriptions() -> None:
    result = list(transaction_descriptions(transaction))
    correct_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert len(result) == len(correct_descriptions)
    for item in range(len(correct_descriptions)):
        assert result[item] == correct_descriptions[item]


def test_card_number_generator() -> None:
    result = list(card_number_generator(1, 5))
    correct_card_number = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == correct_card_number
