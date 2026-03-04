import sys
sys.path.append("../src")
#TODO make it with 'pip install -e.'
from math_demo import (add, add_with_bug)

def test_addition():
    assert add(2, 2) == 4
    print("Test BASIC ADDITION")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return"
    assert add_with_bug(0, 0) == 0
    print("Test BUGGED ADDITION PASSED")
    assert add_with_bug(6, 7) == 13


if __name__ == "main":
    test_addition()
