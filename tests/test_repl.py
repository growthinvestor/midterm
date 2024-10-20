from calculator.repl import REPL
from unittest.mock import patch, MagicMock

@patch('builtins.input', side_effect=['add', '2', '3'])
def test_repl_add(mock_input):
    repl = REPL()
    with patch('builtins.print') as mock_print:
        repl.start()
    mock_print.assert_called_with("Result: 5")

@patch('builtins.input', side_effect=['subtract', '5', '2'])
def test_repl_subtract(mock_input):
    repl = REPL()
    with patch('builtins.print') as mock_print:
        repl.start()
    mock_print.assert_called_with("Result: 3")
