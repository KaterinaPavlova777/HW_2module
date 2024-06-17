import json
import logging
from typing import Any, List

import requests

from src.service import headers

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_data(path: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """
    logger.info(f"get_transactions_data {path}")
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                result_1: Any = []
                logger.info(f"the resulting list {result_1}")
                return result_1
            if isinstance(data, List) or data is None:
                result_2: Any = data
                logger.info(f"the resulting list {result_2}")
                return result_2
            else:
                result_3: Any = []
                logger.info(f"the resulting list {result_3}")
                return result_3
    except FileNotFoundError:
        result_4: Any = []
        logger.info(f"the resulting list {result_4}")
        return result_4


def get_sum_of_transaction(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """
    logger.info(f"start get_sum_of_transaction {transaction}")

    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

    response = requests.get(url, headers=headers).json()

    result = response["result"]

    logger.info(f"sum {result}")

    return float(result)
