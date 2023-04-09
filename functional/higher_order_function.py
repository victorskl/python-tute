"""
Higher Order Functions in Python

Python Higher-Order Functions and Decorators
https://www.hackerearth.com/practice/python/functional-programming/higher-order-functions-and-decorators/tutorial/

Higher Order Functions in Python
https://www.geeksforgeeks.org/higher-order-functions-in-python/
"""


# Functions are treated as first-class citizen and/or Objects
# So. We can do a `function` like we do for a `variable` -- i.e. assignment, pass and/or return around as argument


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):  # <<< greet is HOF
    greeting = func("Hi, I am created by a function passed as an argument.")  # store the function in a variable
    return greeting  # called the pass-in function with modifier value, and return this function


# ---


# Decorator

def check_decorator(f):
    # write your code here or your wrapping function
    # return the wrapping function
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        # print(res)
        if isinstance(res, dict):
            print("checked that the return value is dict")
            return res

    return wrapper


@check_decorator
def my_code(args):
    # original functionality
    return {'lang': args}


# Using this skeleton as an example, giving the @ operator on top of the function
# is the same as writing check_decorator(my_code(args)).


# ---


# Closure

def add_coe():
    _FIVE = 5  # function internal business logic, or a constant, or say a coefficient value of 5

    def add(arg):  # nested function
        return arg + _FIVE

    return add


def create_adder(x):
    def adder(y):
        return x + y

    return adder


# ---


if __name__ == '__main__':
    print('-' * 64)

    print(shout('hello'))

    yell = shout  # assigning function to a variable

    print(yell('hello'))

    print(greet(shout))
    print(greet(whisper))

    # ---

    print('-' * 64)

    print(my_code("python"))

    # ---

    print('-' * 64)

    closure = add_coe()  # function assignment
    print(closure(1))  # output 6
    print(closure(2))  # output 7

    add_15 = create_adder(15)
    print(add_15(10))
