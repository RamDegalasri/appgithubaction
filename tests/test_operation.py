from src.math_operations import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert subtract(5, 3) == 2
    assert subtract(4, 3) == 1
    assert subtract(3, 3) == 0
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 1) == 0
    assert multiply(1, 0) == 0
    assert multiply(1, 1) == 1
    assert multiply(1, -1) == -1
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 0) == 0
    assert multiply(0, 1) == 0
    assert multiply(0, -1) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 1) == 0
    assert divide(1, 0) == 0
    assert divide(1, 1) == 1
    assert divide(1, -1) == -1
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    assert divide(0, 0) == 0
    assert divide(0, 1) == 0
    assert divide(0, -1) == 0

def test_power():
    assert power(2, 3) == 8
    assert power(-1, 1) == -1
    assert power(0, 1) == 0
    assert power(1, 0) == 0
    assert power(1, 1) == 1
    assert power(1, -1) == -1
    assert power(-1, 1) == -1
    assert power(-1, -1) == 1
    assert power(0, 0) == 0
    assert power(0, 1) == 0
    assert power(0, -1) == 0