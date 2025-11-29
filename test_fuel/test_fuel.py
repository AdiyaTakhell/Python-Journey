import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("0/1") == 0
    assert convert("5/5") == 100

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("3-4")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("3/4/5")

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


