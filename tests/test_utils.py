import json
import os
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.utils import get_transactions_data, read_from_csv_file, read_from_xlsx_file


@patch("builtins.open", create=True)
def test_get_transactions_data(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])

    assert get_transactions_data(os.path.join("..", "data", "operations.json")) == [{"test": "test"}]
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf-8")


def test_get_sum_transactions() -> None:
    mock_random = Mock(return_value=351.383168)
    assert mock_random() == 351.383168


@patch("pandas.read_csv")
def test_read_from_csv_file(mock_read_excel: Mock) -> None:
    mock_read_excel.return_value = DataFrame({"test": ["test"]})
    assert read_from_csv_file(os.path.join("..", "data", "transactions.csv")) == [{"test": "test"}]


@patch("pandas.read_excel")
def test_read_from_xlsx_file(mock_read_excel: Mock) -> None:
    mock_read_excel.return_value = DataFrame({"test": ["test"]})
    assert read_from_xlsx_file(os.path.join("..", "data", "transactions_excel.xlsx")) == [{"test": "test"}]
