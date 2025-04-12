"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.

gauge expects an int and returns a str that is:
- "E" if that int is less than or equal to 1,
- "F" if that int is greater than or equal to 99,
- and "Z%" otherwise, wherein Z is that same int.

def main():
    ...

def convert(fraction):
    ...

def gauge(percentage):
    ...

if __name__ == "__main__":
    main()

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_fuel.py
"""

from fuel import convert, gauge
import pytest


def test_c_format():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        convert("12")
    with pytest.raises(ValueError):
        convert("AAB")
    with pytest.raises(ValueError):
        convert("A/B")


def test_c_X_greater_than_Y():
    with pytest.raises(ValueError):
        convert("3/2")


def test_c_y_is_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_g_E():
    assert gauge(1) == "E"
    assert gauge(0.1) == "E"
    assert gauge(0) == "E"


def test_g_F():
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"


def test_g_num():
    assert gauge(50) == "50%"
    assert gauge(78) == "78%"
