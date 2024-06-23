import os

from src.processing import filter_list_by_state, sort_data
from src.utils import find_transaction, get_transactions_data, read_from_csv_file, read_from_xlsx_file
from src.widget import disguised_card_or_check, reformat_data


def main() -> None:
    """
    Основная логика проекта с пользователем и связывание функциональности между собой.
    """
    transactions_data = None

    print(
        """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из json файла
    2. Получить информацию о транзакциях из csv файла
    3. Получить информацию о транзакциях из xlsx файла"""
    )

    user_input_choose_file = int(input())

    if user_input_choose_file == 1:
        transactions_data = get_transactions_data(os.path.join("data", "operations.json"))
        print("Для обработки выбран json файл.")
    elif user_input_choose_file == 2:
        transactions_data = read_from_csv_file(os.path.join("data", "transactions.csv"))
        print("Для обработки выбран csv файл.")
    elif user_input_choose_file == 3:
        transactions_data = read_from_xlsx_file(os.path.join("data", "transactions_excel.xlsx"))
        print("Для обработки выбран xlsx файл.")

    print(
        """Программа: Введите статус по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    user_input_status = input().upper()

    if user_input_status == "EXECUTED" or user_input_status == "CANCELED" or user_input_status == "PENDING":
        print(f'Операции отфильтрованы по статусу "{user_input_status}"')
        filtered_list = filter_list_by_state(transactions_data, user_input_status)
    else:
        print(f'Статус операции "{user_input_status}" недоступен.')
        print(
            """Введите статус по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user_input_status_2 = input().upper()
        filtered_list = filter_list_by_state(transactions_data, user_input_status_2)

    print("Отсортировать операции по дате? Да/Нет")
    user_input_sort_by_data = input().title()
    if user_input_sort_by_data == "Да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_increase_or_decrease = input().lower()
        if user_input_increase_or_decrease == "по убыванию":
            sorted_list_by_data = sort_data(filtered_list, True)
        else:
            sorted_list_by_data = sort_data(filtered_list, False)
    else:
        sorted_list_by_data = filtered_list

    print("Выводить только рублевые тразакции? Да/Нет")
    user_input_rub_or_not = input().lower()
    if user_input_rub_or_not == "да":
        transactions_rub_only = []
        for transaction in sorted_list_by_data:
            if "currency_code" in transaction and transaction["currency_code"] == "RUB":
                transactions_rub_only.append(transaction)
            elif "operationAmount" in transaction and transaction["operationAmount"]["currency"]["code"] == "RUB":
                transactions_rub_only.append(transaction)
        sorted_list_by_data = transactions_rub_only
    else:
        sorted_list_by_data = filtered_list

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input_certain_word = input().lower()
    if user_input_certain_word == "да":
        print("Введите слово, по которому хотите отфильтровать список транзакций.")
        certain_word = input()
        user_certain_word = find_transaction(sorted_list_by_data, certain_word)
        print("Распечатываю итоговый список транзакций...")
    else:
        print("Распечатываю итоговый список транзакций...")

    if len(sorted_list_by_data) == 0:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
    else:
        if user_input_rub_or_not == "да" and user_input_certain_word == "да":
            print(f"Всего банковских операций в выборке: {len(user_certain_word)}")
            print(user_certain_word)
        for transaction in sorted_list_by_data:
            data = transaction["date"]
            desc = transaction["description"]
            out = str(transaction.get("from", "None card/account"))
            to = str(transaction["to"])
            amount = transaction["operationAmount"]["amount"]
            print(
                f"""{reformat_data(data)} {desc}
        {disguised_card_or_check(out)} -> {disguised_card_or_check(to)}
        Сумма: {amount} руб.
        """
            )

        else:
            print(f"Всего банковских операций в выборке: {len(sorted_list_by_data)}")
            for transaction in sorted_list_by_data:
                data = transaction["date"]
                desc = transaction["description"]
                out = str(transaction.get("from", "None card/account"))
                to = str(transaction["to"])
                amount = transaction["operationAmount"]["amount"]
                print(
                    f"""{reformat_data(data)} {desc}
            {disguised_card_or_check(out)} -> {disguised_card_or_check(to)}
            Сумма: {amount}
            """
                )


if __name__ == "__main__":
    main()
