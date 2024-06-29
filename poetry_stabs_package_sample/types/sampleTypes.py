"""This is a sample module for the poetry_stabs_package_sample package."""

import typing
import enum

# これはtypeAliasなので型エラーは起きない
myId: typing.TypeAlias = int
NewTypeId = typing.NewType("NewTypeId", int)


def convert_id(id: int) -> myId:
    """Convert id."""
    return id


def convert_new_type_id(id: int) -> NewTypeId:
    """Convert id."""
    return NewTypeId(id)


class Emotion(enum.IntEnum):
    """Emotion class."""

    HAPPY = 1
    SAD = 2
    ANGRY = 3
    SURPRISED = 4
    UNKNOWN = 5
