import pytest
import re

from um import count

def test_count_exact_match():
    assert count("um") == 1

def test_count_case_insensitive():
    assert count("Um uM UM um") == 4

def test_count_with_surrounding_text():
    assert count("hello um world") == 1

def test_count_with_punctuation():
    assert count("um, hello. um!") == 2

def test_count_not_partial():
    assert count("umbrella is nice but um is better") == 1  # Ensures "um" is not counted inside words

def test_count_no_occurrences():
    assert count("hello world") == 0

if __name__ == "__main__":
    pytest.main()