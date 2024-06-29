"""This is a sample module for the poetry_stabs_package_sample package."""

import typing


def sample2sample(collable: typing.Callable[[], str]) -> str:
    """Sample2.

    this function suppose to call the util.usefull2

    Args:
        collable: Callable[[], str]: Callable.

    Returns:
        str: Return value.
    """
    print("sample2")
    ret = collable()
    return ret
