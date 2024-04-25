import pytest

from src.masks import disguised_card, disguised_check


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1111111111111111", "1111 11** **** 1111"),
    ],
)
def test_disguised_card(string: str, expected_result: str) -> None:
    assert disguised_card(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("11111111111111111111", "**1111"),
    ],
)
def test_disguised_check(string: str, expected_result: str) -> None:
    assert disguised_check(string) == expected_result
