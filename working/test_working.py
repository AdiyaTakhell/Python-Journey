import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1:30 PM to 3:45 AM") == "13:30 to 03:45"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("invalid input")
    with pytest.raises(ValueError):
        convert("25 AM to 10 PM")
    with pytest.raises(ValueError):
        convert("10:70 AM to 2 PM")

