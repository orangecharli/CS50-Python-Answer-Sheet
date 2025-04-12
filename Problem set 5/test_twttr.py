"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

"""
from twttr import shorten
import pytest

def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("hello world") == "hll wrld"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_int():
    with pytest.raises(TypeError):
        shorten(3333)

def test_int():
    assert shorten("hey, there") == "hy, thr"

def test_str_num():
    assert shorten("333") == "333"


