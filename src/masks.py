import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def disguised_card(user_card: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    logger.info(f"start disguised_card {user_card}")
    result = f"{user_card[0:4]} {user_card[4:6]}** **** {user_card[12:16]}"
    logger.info(f"mask {result}")
    return result


def disguised_check(user_check: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    logger.info(f"start disguised_check {user_check}")
    result = f"**{user_check[-4:]}"
    logger.info(f"mask {result}")
    return result
