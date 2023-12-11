"""
Mastering Monad Design Patterns: Simplify Your Python Code and Boost Efficiency - Hamzza K
https://dev.to/hamzzak/mastering-monad-design-patterns-simplify-your-python-code-and-boost-efficiency-kal

The IO monad is a way of dealing with input and output in a purely functional way.

In Python, the IO monad can be implemented using a class with a single method call that takes no arguments and returns
the result of the IO operation. Here's an example of how you might use the IO monad in Python to read a file and
print its contents.
"""


class IO:
    def __init__(self, effect):
        self.effect = effect

    def __call__(self):
        return self.effect()


def read_file(filename):
    def read_file_effect():
        with open(filename, 'r') as f:
            return f.read()

    return IO(read_file_effect)


def print_contents(contents_):
    def print_effect():
        print(contents_)

    return IO(print_effect)


if __name__ == '__main__':
    """
    In this example, we call read_file() to create an IO object that reads the contents of a file. We then call the 
    call() method of this object to execute the IO operation and retrieve the contents of the file. We store the 
    contents in the contents variable and pass it as an argument to print_contents() which creates another IO object 
    that prints the contents to the console. Finally, we call the call() method of the print_contents() object to 
    execute the IO operation and print the contents of the file to the console.    
    """
    # chain the IO operations manually
    contents = read_file('__init__.py')()  # IIFE
    print_contents(contents)()
