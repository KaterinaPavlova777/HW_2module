import json
import os
from unittest.mock import Mock, patch

from src.utils import get_transactions_data


@patch("builtins.open", create=True)
def test_get_transactions_data(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])

    assert get_transactions_data(os.path.join("..", "data", "operations.json")) == [{"test": "test"}]
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf-8")


def test_get_sum_transactions() -> None:
    mock_random = Mock(return_value=351.383168)
    assert mock_random() == 351.383168
