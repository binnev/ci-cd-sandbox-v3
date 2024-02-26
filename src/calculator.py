def add(a: int, b: int) -> int:
    """
    A function for adding two integers

    Args:
        a: the first number
        b: the second number

    Returns:
        the sum of the two numbers: `a + b`
    """
    return _add(a, b)


def _add(a: int, b: int) -> int:
    """
    docstring

    :param a:
    :param b:
    :return:
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """
    A function for multiplying two integers.

    Args:
        a: the first number
        b: the second number

    Returns:
        the first number times the second number: `a * b`
    """
    return a * b


def subtract(a: int, b: int) -> int:
    """
    A function for subtracting two integers

    Args:
        a: the first number
        b: the second number

    Returns:
        the first number minus the second: `a - b`
    """
    return a - b


def _private(stuff: str) -> str:
    """
    Args:
        stuff: a string

    Returns:
        the same stuff
    """
    print(stuff)
    return stuff
