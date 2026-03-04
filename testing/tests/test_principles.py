import sys
sys.path.append("../src")
#TODO make it with 'pip install -e.'
from math_demo import (add, add_with_bug, calculate_tax_with_bug, calculate_tax)

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

def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-7, 0) == -7
    print("Test ADDITION REASONABLE PASS")

def test_addition_communication():
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("Test ADDITION COMMUNICATION PASS")

def test_tax_calculation():
    # using only integers limits test case
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30
    assert calculate_tax_with_bug(0) == 0
    print("Test ADDITION calculation PASS")


if __name__ == "main":
    test_addition()
    test_addition_duplicated()
    test_addition_overcomplex()
    test_addition_reasonable()
    test_addition_with_bug()
    test_tax_calculation()
