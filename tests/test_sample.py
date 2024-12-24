# test_sample.py
import pytest

# Simple test case
def test_addition():
    assert 1 + 1 == 2

# Test case with a failure (for demonstration)
def test_subtraction():
    assert 2 - 1 == 2  # This will fail

# Example of a test with a parameter
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (5, 5, 10), (10, 5, 15)])
def test_addition_with_params(a, b, expected):
    assert a + b == expected
