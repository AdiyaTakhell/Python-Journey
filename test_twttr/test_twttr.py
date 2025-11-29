import pytest
from twttr import shorten

def test_function():
    assert shorten("test_twitter") == "tst_twttr"
    assert shorten("test_Two") == "tst_Tw"
    assert shorten("tes'1t") == "ts'1t"
    assert shorten("HELLO") == "HLL"
    assert shorten("What’s up?!") == "Wht’s p?!"
    assert shorten("CS50") == "CS50"
