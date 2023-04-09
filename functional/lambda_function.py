"""
https://realpython.com/python-lambda/
"""
import dis


def add_one(x):
    return x + 1


if __name__ == '__main__':
    print(add_one(1))

    # `lambda` is anonymous function

    print((lambda x: x + 1)(1))

    add_one_anonymous_function = lambda x: x + 1

    print(type(add_one_anonymous_function))
    print(add_one_anonymous_function(1))

    print((lambda x, y: x + y)(2, 3))  # IIFE (iffy!) https://developer.mozilla.org/en-US/docs/Glossary/IIFE

    # --- HOF

    hof = lambda x, func: x + func(x)

    print(hof(2, lambda x: x * x))

    print(hof(2, lambda x: x + 3))

    # --- runtime: <function <lambda> 0xMemAddress>

    add = lambda x, y: x + y
    print(type(add))
    dis.dis(add)  # peek as bytecode representation
    print(add)

    # tl;dr
    # use sparingly! :)
