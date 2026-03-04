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
    assert add_with_bug(6, 7) == 13 # will fail here
    
def test_addition_duplicated():
    # is it real good test (relies on absence)
    assert add(2, 3) == 2 + 3
    
def test_addition_overcomplex():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum(i, j)
            assert add(-i, -j) == sum(-i, -j)
            assert add(i, j) == sum(i, j)
            assert add(-i, -j) == sum(-i, -j)


if __name__ == "main":
    test_addition()
