"""Tests for add()."""
from add import add


def test_add() -> None:
    """add() sums two positive integers."""
    assert add(2, 3) == 5
