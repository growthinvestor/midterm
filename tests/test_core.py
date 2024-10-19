from calculator import core

def test_add(sample_values):
    a, b = sample_values
    assert core.add(a, b) == 5

def test_subtract(sample_values):
    a, b = sample_values
    assert core.subtract(a, b) == -1
