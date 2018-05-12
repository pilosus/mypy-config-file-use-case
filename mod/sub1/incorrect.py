from typing import Iterable, Generator

def my_map(fun: function, it: Iterable) -> Generator:
    for i in it:
        yield fun(i)

if __name__ == '__main__':
    my_map('a', 666)
