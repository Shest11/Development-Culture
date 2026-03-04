import sys
sys.path.append("../src")
#TODO make it with `pip install -e.`
from math_demo import add

def test_addition():
    assert add(2, 2) == 4
    print("Test BASIC ADDITION")

if __name__ == "main":
    test_addition()