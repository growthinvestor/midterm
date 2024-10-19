from calculator.repl import CalculatorREPL
from io import StringIO
import sys

def test_repl_add(monkeypatch):
    repl = CalculatorREPL()
    inputs = "add 2 3\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(inputs))
    monkeypatch.setattr('sys.stdout', StringIO())
    repl.cmdloop()
    output = sys.stdout.getvalue()
    assert "5.0" in output
