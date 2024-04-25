from typing import Dict, List


def filter_list_by_state(input_data: List[Dict[str, str | int]], state: str) -> List[Dict[str, str | int]]:
    """
    Принимает список словарей и значение для ключа и возвращает новый список, содержащий словари,
    у которых ключ state содержит переданное в функцию значение
    """
    output_data = []
    for dict_ in input_data:
        if dict_["state"] == state:
            output_data.append(dict_)
    return output_data


def sort_data(input_data: List) -> List:
    """
    Принимает на вход список словарей и возвращает список, в котором исходные словари отсортированы по убыванию даты.
    """
    return sorted(input_data, key=lambda x: x.get("date"), reverse=True)
