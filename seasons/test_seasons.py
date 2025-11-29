from seasons import convert_to_words

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert convert_to_words(1578240) == "One million, five hundred seventy-eight thousand, two hundred forty minutes"
