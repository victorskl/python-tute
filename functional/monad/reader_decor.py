"""
Mastering Monad Design Patterns: Simplify Your Python Code and Boost Efficiency - Hamzza K
https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal

In this example, the reader function takes a function as an argument and returns a wrapped function. The wrapped
function takes an additional keyword argument, config, which is used to pass a configuration dictionary to the function.

By decorating a function with the reader decorator, you are creating a new function that expects a config keyword
argument and passes it to the decorated function. This allows you to separate the configuration data from the rest of
your function's logic.
"""

from typing import Dict, Callable, TypeVar

T = TypeVar('T')


def reader(f: Callable[..., T]) -> Callable[..., T]:
    def wrapped(*args, **kwargs):
        config = kwargs.get('config')
        if config is None:
            raise ValueError('config is None')
        if not isinstance(config, dict):
            raise TypeError('config is not a dictionary')
        return f(config, *args)

    return wrapped


@reader
def greet(config: Dict[str, str]) -> str:
    """
    In the example code, the greet function is decorated with the reader decorator. This means that when you call the
    greet function using greet(config={"name": "Beta"}), the config dictionary is passed to the decorated function,
    and the resulting string is returned.

    The greet function itself takes a config dictionary as its argument and returns a string greeting the person whose
    name is specified in the config dictionary. The config argument is passed to the greet function via the wrapped
    function created by the reader decorator.

    :param config:
    :return:
    """
    return f"Hi, {config['name']}"


@reader
def saluer(config) -> str:
    return f"Bonjour, {config['name']}"


@reader
def aloha(config) -> str:
    return f"Hello, {config}"


if __name__ == '__main__':
    result = greet(config={'name': 'Beta'})
    print(result)  # Hi, Beta

    print(saluer(config={'name': 'Beta'}))

    try:
        print(aloha(config=""))  # simulate TypeError
    except TypeError:
        pass
