"""Simple calculator utilities."""

from typing import Union

Number = Union[int, float]


def add_numbers(a: Number, b: Number) -> Number:
    """Return the sum of two numbers.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The sum of `a` and `b`.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b


def subtract_numbers(a: Number, b: Number) -> Number:
    """Return the difference of two numbers (`a - b`).

    Args:
        a: Minuend.
        b: Subtrahend.

    Returns:
        The result of subtracting `b` from `a`.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a - b


__all__ = ["add_numbers", "subtract_numbers"]


def _ensure_number(value: object, name: str) -> None:
    """Raise TypeError if `value` is not an int or float.

    Args:
        value: The value to check.
        name: The parameter name (used in the error message).

    Raises:
        TypeError: If `value` is not an instance of `int` or `float`.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be an int or float, got {type(value).__name__}")
