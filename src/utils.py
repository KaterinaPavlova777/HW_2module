import json
from typing import List

import requests

from src.service import headers


def get_transactions_data(path: str) -> List | None:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                return []
            if isinstance(data, List) or data is None:
                return data
            else:
                return []
    except FileNotFoundError:
        return []


def get_sum_of_transaction(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

    response = requests.get(url, headers=headers).json()

    return float(response["result"])
