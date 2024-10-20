import pytest
from dotenv import load_dotenv  # Import load_dotenv
import os  # Import os to access environment variables
import sys

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


from calculator.plugins.cube_plugin import ExamplePlugin

def test_greet():
    plugin = ExamplePlugin()
    assert plugin.greet("World") == "Hello, World!"
