from typing import Iterable, Generator, Callable

def my_map(fun: Callable, it: Iterable) -> Generator:
    for i in it:
        yield fun(i)

if __name__ == '__main__':
    my_map(lambda x: x ** 2, range(10))
