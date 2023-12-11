"""
https://jasondelaat.github.io/pymonad_docs/explanations/whats-a-monad.html

A monad actually is function composition
"""


class Logging:
    def __init__(self, result_, message):
        self.result = result_
        self.message = message

    def bind(self, g):
        # The infamous bind
        gx = g(self.result)
        return Logging(gx, self.message + gx.message)

    def __str__(self):
        return self.message


def add_7(x):
    return Logging(x + 7, 'Adding 7 to input {}\n'.format(x))


def mul_5(x):
    return Logging(x * 5, 'Multiplying input {} by 5\n'.format(x))


def monad_compose(f, g):
    return lambda x: f(x).bind(g)


if __name__ == '__main__':
    composed_arithmetic = monad_compose(add_7, mul_5)  # function composition
    result = composed_arithmetic(6)
    print(result)

    # Adding 7 to input 6
    # Multiplying input 13 by 5
