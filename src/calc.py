def add(a: int, b: int) -> int:
    """
    Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Subtract the second number from the first.

    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.

    Returns:
        int: The result of the subtraction.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Divide the first number by the second.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("The denominator cannot be zero.")
    return a / b
