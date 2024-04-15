def disguised_card(user_card: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    return f"{user_card[0:4]} {user_card[4:6]}** **** {user_card[12:16]}"


def disguised_check(user_check: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    return f"**{user_check[-4:]}"
