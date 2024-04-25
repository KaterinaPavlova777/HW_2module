import pytest

from src.widget import disguised_card_or_check, reformat_data


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_disguised_card_or_check(string: str, expected_result: str) -> None:
    assert disguised_card_or_check(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_reformat_data(string: str, expected_result: str) -> None:
    assert reformat_data(string) == expected_result
