from numb3rs import validate
import pytest


def test_valid():
    assert validate("1.1.1.1")==True
    assert validate("192.152.50.2")
def test_invalid():
    assert validate("cat")==False
    assert validate("550.2.21.21")==False