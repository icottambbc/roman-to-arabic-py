from index import convert

def test_fails_for_number():
    assert convert(1) == False

def test_X():
    assert convert("X") == 10

def test_IX():
    assert convert("XXIX") == 29

def test_MMXI():
    assert convert("MMXI") == 2011

def test_MMMXI():
    assert convert("MMMXI") == 3011

def test_MCMXCIX():
    assert convert("MCMXCIX") == 1999

def test_CM():
    assert convert("CM") == 900

def test_CD():
    assert convert("CD") == 400

def test_XL():
    assert convert("XL") == 40

def test_CMXLVII():
    assert convert("CMXLVII") == 947


    

    

    

    