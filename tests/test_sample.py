"""Tests for the sample module."""

from poetry_stabs_package_sample.sample import add


def test_add() -> None:
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, -100) == 0
