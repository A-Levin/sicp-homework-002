from sum_digits import sum_digits

def test_single_digit():
    assert sum_digits(5) == 5

def test_two_digits():
    assert sum_digits(12) == 3

def test_three_digits():
    assert sum_digits(123) == 6

def test_with_zeros():
    assert sum_digits(1000) == 1

def test_large_number():
    assert sum_digits(12345) == 15

def test_all_nines():
    assert sum_digits(999) == 27
