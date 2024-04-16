from src import masks


def disguised_card_or_check(user_input: str) -> str:
    """
    Функция принимает на вход номер карты или номер счета и возвращает маску.
    """
    if user_input[0:4] == 'Счет':
        splitted_usercheck_list = list(user_input.split())
        check_name = []
        check_numbers = []
        for i in splitted_usercheck_list:
            if i.isalpha():
                check_name.append(i)
            else:
                check_numbers.append(i)
        return f"Счет {masks.disguised_check(' '.join(check_numbers))}"

    else:
        splitted_usercard_list = list(user_input.split())
        card_name = []
        card_numbers = []
        for i in splitted_usercard_list:
            if i.isalpha():
                card_name.append(i)
            else:
                card_numbers.append(i)
    if len(card_numbers) > 1:
        return f"{' '.join(card_name)} {card_numbers[0]} {card_numbers[1][0:2]}** **** {card_numbers[3]}"
    return f"{' '.join(card_name)} {masks.disguised_card(' '.join(card_numbers))}"
