"""
Mastering Monad Design Patterns: Simplify Your Python Code and Boost Efficiency - Hamzza K
https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal
"""


class Maybe:
    """
    Maybe class represents a computation that may or may not return a value.

    The add_one and double functions represent computations.
    These functions can be chained together using the bind method to create more complex computations
    that can handle error conditions and side effects.

    Note that the Monad design pattern is not a commonly used pattern in Python,
    as it is more commonly associated with functional programming languages like Haskell.

    However, the pattern can still be useful in certain situations where you need to chain
    computations together in a more modular and reusable way.
    """

    def __init__(self, value):
        self._value = value

    def bind(self, func):
        """
        The bind method takes a function as input and returns a new Maybe instance
        that represents the result of applying the function to the original value, if it exists.

        :param func:
        :return:
        """
        if self._value is None:
            return Maybe(None)
        else:
            return Maybe(func(self._value))

    def or_else(self, default):
        if self._value is None:
            return Maybe(default)
        else:
            return self

    def unwrap(self):
        return self._value

    def __or__(self, other):
        """
        The | operator can be used to combine two Maybe instances, returning the first one that contains a value.

        :param other:
        :return:
        """
        return Maybe(self._value or other.unwrap())

    def __str__(self):
        if self._value is None:
            return 'Nothing'
        else:
            return 'Just {}'.format(self._value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Maybe):
            return self._value == other._value
        else:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __bool__(self):
        return self._value is not None


def add_one(x):
    return x + 1


def double(x):
    return x * 2


if __name__ == '__main__':
    result = Maybe(3).bind(add_one).bind(double)
    print(result)  # Just 8

    result = Maybe(None).bind(add_one).bind(double)
    print(result)  # Nothing

    result = Maybe(None).bind(add_one).bind(double).or_else(10)
    print(result)  # Just 10

    result = Maybe(None) | Maybe(1)
    print(result)  # Just 1
