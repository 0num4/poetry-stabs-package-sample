"""This is a sample module for the poetry_stabs_package_sample package."""

import typing

# これはtypeAliasなので型エラーは起きない
myId: typing.TypeAlias = int
NewTypeId = typing.NewType("NewTypeId", int)


def convert_id(id: int) -> myId:
    """Convert id."""
    return id


def convert_new_type_id(id: int) -> NewTypeId:
    """Convert id."""
    return NewTypeId(id)
