# lambdaに型を付けるテスト
from typing import Callable


def main() -> None:
    # def test_func(func: Callable[[int, int], int]) -> None:
    #     print(func(1, 2))

    # def add(a: int, b: int) -> int:
    #     return a + b
    l: Callable[[int], int] = lambda x: x + 1
    l(34)
    nandemo(4, 6)


def nandemo(*args) -> None:
    print(len(args))
