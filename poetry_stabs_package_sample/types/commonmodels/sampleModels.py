"""This is a sample module for the poetry_stabs_package_sample package."""

import typing


class CommonModel(typing.TypedDict):
    """CommonModel."""

    id: int
    name: str
    age: int
    is_active: bool
    created_at: str
    updated_at: str


def create_common_model(id: int) -> CommonModel:
    """CommonModel."""
    return {
        "id": id,
        "name": "test",
        "age": 20,
        "is_active": True,
        "created_at": "2021-01-01 00:00:00",
        "updated_at": "2021-01-01 00:00:00",
    }
