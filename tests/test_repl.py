import pytest
from dotenv import load_dotenv  # Import load_dotenv
import os  # Import os to access environment variables
import sys


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Load environment variables from .env file

load_dotenv()

# Import your classes here
from calculator.core import Calculator
from calculator.repl import REPL

# Test case for calculator addition
def test_calculator_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5

# Test REPL for addition command
def test_repl_add(monkeypatch, capfd):
    """Test the REPL for addition command."""
    # Simulate user entering '1' (for Add), '2', '3', and then '6' (for Quit)
    inputs = iter(['1', '2', '3', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    repl = REPL()

    with pytest.raises(SystemExit):  # Expect SystemExit when 'quit' is called
        repl.start()

    # Capture printed output
    captured = capfd.readouterr()

    # Check if the expected output was printed
    assert "Result: 5.0" in captured.out  # Ensure you match the expected output format

# Test REPL for subtraction command
def test_repl_subtract(monkeypatch, capfd):
    """Test the REPL for subtraction command."""
    # Simulate user entering '2' (for Subtract), '5', '2', and then '6' (for Quit)
    inputs = iter(['2', '5', '2', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    repl = REPL()

    with pytest.raises(SystemExit):  # Expect SystemExit when 'quit' is called
        repl.start()

    # Capture printed output
    captured = capfd.readouterr()

    # Check if the expected output was printed
    assert "Result: 3.0" in captured.out  # Ensure you match the expected output format

# Test REPL for history command
def test_repl_history(monkeypatch, capfd):
    """Test the REPL for history command."""
    # Simulate user entering '1' (for Add), '2', '3', '5' (for History), and then '6' (for Quit)
    inputs = iter(['1', '2', '3', '5', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    repl = REPL()

    with pytest.raises(SystemExit):  # Expect SystemExit when 'quit' is called
        repl.start()

    # Capture printed output
    captured = capfd.readouterr()

    # Check if the history output was printed
    assert "History" in captured.out  # Ensure you match the expected output format
