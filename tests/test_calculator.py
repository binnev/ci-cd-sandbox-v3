from src.calculator import add, subtract


def test_add():
    assert add(1, 1) == 2


def test_subtract():
    assert subtract(2, 1) == 1
