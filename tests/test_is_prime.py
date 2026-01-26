from is_prime import is_prime

def test_zero():
    assert is_prime(0) == False

def test_one():
    assert is_prime(1) == False

def test_two():
    assert is_prime(2) == True

def test_three():
    assert is_prime(3) == True

def test_four():
    assert is_prime(4) == False

def test_seven():
    assert is_prime(7) == True

def test_nine():
    assert is_prime(9) == False

def test_eleven():
    assert is_prime(11) == True

def test_large_prime():
    assert is_prime(97) == True

def test_large_composite():
    assert is_prime(100) == False
