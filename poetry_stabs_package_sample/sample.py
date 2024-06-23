"""lambdaに型を付けるテスト."""

from typing import Callable


def main() -> None:
    """メイン関数."""
    # def test_func(func: Callable[[int, int], int]) -> None:
    #     print(func(1, 2))

    # def add(a: int, b: int) -> int:
    #     return a + b
    l: Callable[[int], int] = lambda x: x + 1  # noqa: E731, E741
    l(34)
    nandemo(4, 6)


def nandemo(*args, **kwargs) -> None:
    """可変長引数のテスト関数."""
    print(len(args))
    print(len(kwargs))


def add(a: int, b: int) -> int:
    """testをするためのadd関数."""
    return a + b


if __name__ == "__main__":
    main()
