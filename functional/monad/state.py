"""
Mastering Monad Design Patterns: Simplify Your Python Code and Boost Efficiency - Hamzza K
https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal
"""


class State:
    """
    The state monad allows you to encapsulate a stateful computation as a pure function that takes an initial state and
    returns a new state and a result. The state is typically represented as a data structure, and the function performs
    computations that update the state as needed. The state monad is often used in functional languages like Haskell and
    Scala, but it can also be implemented in Python.

    In Python, you can implement the state monad using classes and closures. The basic idea is to define a class that
    represents a stateful computation, and use closures to create new stateful computations that depend on the current
    state. The call method of the class is used to define the actual computation, and it returns a new instance of the
    class with an updated state and a result.

    In this example, we define a State class that encapsulates a stateful computation.
    The init method initializes the state, which is represented as a tuple with two values: the count and the result.
    The call method is the actual computation, which returns a tuple containing the result and a new instance of the
    State class with an updated state.

    We then create an instance of the State class called counter that represents the stateful computation that counts
    the number of times it is called. We call the computation multiple times using a loop, and print the current count
    and result after each call.

    The benefits of using the state monad in Python include the ability to write pure functions that encapsulate
    stateful computations, which can improve code clarity and maintainability. By separating the stateful computation
    from the rest of the code, you can write more modular and testable code that is easier to reason about.
    Additionally, the use of closures can make it easier to write stateful computations that depend on the
    current state, and can simplify code that would otherwise be more complex to write and maintain.
    """

    def __init__(self, state):
        self.state = state

    def __call__(self, value):
        # print(self.state[0], self.state[1], value)
        return self.state[1], State((self.state[0] + 1, value))


if __name__ == '__main__':
    # create a stateful computation that counts the number of times it is called
    counter = State((0, 0))

    # call the computation multiple times and print the current count
    for i in range(5):
        result, counter = counter(i)
        print(f"Computation result: {result}, count: {counter.state[0]}")

    # Computation result: 0, count: 1
    # Computation result: 0, count: 2
    # Computation result: 1, count: 3
    # Computation result: 2, count: 4
    # Computation result: 3, count: 5
