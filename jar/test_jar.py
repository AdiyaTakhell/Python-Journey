import pytest
from jar import Jar

def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_custom_capacity():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-5)

def test_str_representation():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit_valid():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5

def test_deposit_invalid_overflow():
    jar = Jar(3)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_deposit_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw_valid():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def test_withdraw_invalid_overdraw():
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_withdraw_negative():
    jar = Jar()
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_capacity_property():
    jar = Jar(10)
    assert jar.capacity == 10

def test_size_property():
    jar = Jar(10)
    jar.deposit(4)
    assert jar.size == 4
