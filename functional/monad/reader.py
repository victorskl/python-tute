"""
Mastering Monad Design Patterns: Simplify Your Python Code and Boost Efficiency - Hamzza K
https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal

The Reader monad is a functional programming concept that allows you to pass around an immutable environment to
a function, so that the function can access values from the environment without having to explicitly pass them
as arguments.

In the Reader monad, the environment is modeled as a function that takes a single argument and returns a value.
The function that uses the environment is then wrapped in a monadic context, so that it can be composed with other
monadic functions.
"""

from typing import Any, Callable, TypeVar

T = TypeVar('T')


def reader(f: Callable[[Any], T]) -> Callable[[Any], T]:
    """
    The reader function is a helper function that returns a wrapped function that takes a single argument. The wrapped
    function calls the original function with the argument.

    :param f:
    :return:
    """

    def wrapped(*args):
        return f(*args)

    return wrapped


def greet(name: str) -> str:
    """
    The greet function takes a single argument, name, and returns a string.

    :param name:
    :return:
    """
    return f"Hello, {name}!"


if __name__ == '__main__':
    """
    The greet_reader function is created by calling the reader function with the greet function as an argument. The 
    greet_reader function takes a single argument, name, and returns the result of calling greet with the name argument.
    """
    greet_reader = reader(greet)

    # call greet_reader with the name argument
    result = greet_reader("Alpha")

    print(result)  # output: "Hello, Alpha!"
