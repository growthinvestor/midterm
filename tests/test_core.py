import pytest
import sys
import os  # Import os to access environment variables
from dotenv import load_dotenv  # Import load_dotenv
from calculator.core import Calculator


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Load environment variables from .env file
load_dotenv()

# Your test cases here
def test_calculator_add():
    from calculator.core import Calculator  # Import your classes here
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5

# Add more test cases as needed


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(1, 0)
