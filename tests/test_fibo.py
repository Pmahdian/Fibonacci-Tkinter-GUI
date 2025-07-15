import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fibo_utils import generate_fibonacci

def test_fibonacci_basic():
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(2) == [0, 1]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_zero_and_negative():
    with pytest.raises(ValueError):
        generate_fibonacci(0)
    with pytest.raises(ValueError):
        generate_fibonacci(-3)
