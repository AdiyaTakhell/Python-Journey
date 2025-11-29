from plates import is_valid

def test_valid_plate():
    assert is_valid("CS50") == True

def test_too_short():
    assert is_valid("C") == False

def test_too_long():
    assert is_valid("CS50AB") == False

def test_starts_with_digit():
    assert is_valid("50CS") == False

def test_middle_zero():
    assert is_valid("CS05") == False

def test_alpha_then_digit():
    assert is_valid("CS5A") == False

def test_special_characters():
    assert is_valid("CS!@") == False
