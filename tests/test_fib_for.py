from fib_for import fib

def test_fib_0():
    assert fib(0) == 0

def test_fib_1():
    assert fib(1) == 1

def test_fib_2():
    assert fib(2) == 1

def test_fib_5():
    assert fib(5) == 5

def test_fib_10():
    assert fib(10) == 55

def test_fib_15():
    assert fib(15) == 610
