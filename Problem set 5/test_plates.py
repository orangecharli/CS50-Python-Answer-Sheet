"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

def main():
    ...

def is_valid(s):
    ...

if __name__ == "__main__":
    main()

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_plates.py
"""

from plates import is_valid
import pytest


def test_two_letters():
    assert is_valid("AA102") == True
    assert is_valid("A1002") == False
    assert is_valid("100") == False


def test_length_is_between_2_and_6():
    assert is_valid("AAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAAAAAAA") == False


def test_numbers_in_middle():
    assert is_valid("AA10AA") == False


def test_first_number_0():
    assert is_valid("AAH02") == False


def test_period():
    assert is_valid("AA.10") == False


def test_spaces():
    assert is_valid("A A10") == False
    assert is_valid("  AA100") == False


def test_punctuation():
    assert is_valid("AA100,") == False
    assert is_valid("AA,100") == False
