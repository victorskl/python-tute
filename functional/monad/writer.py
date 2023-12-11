"""
Mastering Monad Design Patterns: Simplify Your Python Code and Boost Efficiency - Hamzza K
https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal

The Writer Monad allows us to perform computations while accumulating a log or other auxiliary information. It is
similar to the Reader monad in that it separates some aspect of your program's behavior (in this case, logging or
accumulation) from the rest of your application logic.

In Python, you can implement the Writer monad using a combination of a tuple and a function that takes a value and
a log, and returns a new value and log. This function is usually called the "writer function".
"""


def writer(value, log_):
    """
    In this example, the writer function takes a value and a log as its arguments and returns a tuple containing the
    value and log.

    :param value:
    :param log_:
    :return:
    """

    return value, log_


def add(x, y):
    """
    The add and multiply functions perform addition and multiplication, respectively, and also generate log messages
    using formatted strings.

    :param x:
    :param y:
    :return:
    """
    result_ = x + y
    log_ = f"Adding {x} and {y} to get {result_}.\n"
    return writer(result_, log_)


def multiply(x, y):
    result_ = x * y
    log_ = f"Multiplying {x} and {y} to get {result_}.\n"
    return writer(result_, log_)


if __name__ == '__main__':
    """
    This demonstrates how the Writer monad can be used to accumulate log messages as your program runs, making it easier
    to debug and understand the behavior of your code.
    
    Another example of the Writer monad might involve accumulating a list of values as your program runs, or maintaining
    a running total of some quantity. The basic idea is the same: use a tuple and a writer function to accumulate values
    or logs, and chain together functions using the partial function to combine them into a larger computation.
    """

    # Chain together add and multiply using the Writer monad
    add_result, add_log = add(2, 3)
    mul_result, mul_log = multiply(add_result, 4)
    result = mul_result
    log = add_log + mul_log
    print(f"Result: {result}")
    print(f"Log: {log}")

    # result: 20
    # log: Adding 2 and 3 to get 5.
    # Multiplying 5 and 4 to get 20.
