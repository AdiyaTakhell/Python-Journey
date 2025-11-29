from bank import value

def test_hello_variants():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("  Hello, friend") == 0

def test_h_prefix_but_not_hello():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20
    assert value("howdy") == 20
    assert value("HYPE!!!") == 20

def test_other_phrases():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("yo") == 100
    assert value("sup") == 100
    assert value("Greetings") == 100

def test_whitespace_and_noise():
    assert value("    hello") == 0
    assert value("   hi") == 20
    assert value("   what's up?") == 100