"""
Higher-Order Functions in Python — map(), filter(), and reduce()
https://medium.com/swlh/higher-order-functions-in-python-map-filter-and-reduce-34299fee1b21
"""
from functools import reduce
from operator import add, mul

if __name__ == '__main__':
    # --- Map

    # Declare a list to be mapped
    seasons = ['spring', 'summer', 'fall', 'winter']

    # Map the list with the string uppercase function
    mapped_seasons = map(str.upper, seasons)

    print(type(mapped_seasons))  # map() return a `map` object
    print(mapped_seasons)  # print `map` object memory address
    print(dir(mapped_seasons))  # print `map` object methods

    # So how do we iterate `map` object to have a look its elements value

    # Convert the map object to a list
    upper_seasons = list(mapped_seasons)
    print(upper_seasons)


    # Declare a function to calculate the difference between predicted and actual target values
    def squared_difference(x, y):
        predicted_y = 3 * x + 5
        difference = predicted_y - y
        return difference * difference


    # Create the x and y values
    x_values = [2, 3, 4, 7]
    y_values = [10, 14.5, 18.5, 25]

    # Calculate the difference
    differences = list(map(squared_difference, x_values, y_values))
    print(differences)

    # --- Filter

    # Declare a list for filtering
    integers = [1, 2, 3, 4, 5, 6, 7]

    # Filter the list
    filtered_integers = filter(lambda x: x % 2 == 0, integers)
    print(filtered_integers)  # print `filter` object memory address

    # Wrap with the list, so that we can iterate over elements -- also
    even_numbers = list(filtered_integers)
    print(even_numbers)

    # Declare a list for filtering
    students = {
        'Aaron': {'phys': 95, 'chem': 80, 'math': 92},
        'David': {'phys': 99, 'chem': 85, 'math': 92},
        'John': {'phys': 92, 'chem': 84, 'math': 89},
        'Danny': {'phys': 93, 'chem': 82, 'math': 91},
        'Zack': {'phys': 97, 'chem': 86, 'math': 93}
    }


    # Define a function for filtering
    def qualify_student(x):
        _, info = x
        condition0 = info['phys'] > 95
        condition1 = info['chem'] > 83
        condition2 = info['math'] > 90
        return condition0 and condition1 and condition2


    # Create a dict of qualified students
    qualified_students = dict(filter(qualify_student, students.items()))
    print(qualified_students)

    # --- Reduce

    # Create a list for reducing
    primes = [2, 3, 5, 7, 11, 13]

    # Reduce the list
    total = reduce(lambda x, y: x + y, primes, 1)  # reduce(function, sequence[, initial]) -> value
    print(total)

    total = reduce(lambda x, y: x + y, primes, 5)
    print(total)


    def factorial(n):
        """
        See https://www.mathsisfun.com/numbers/factorial.html
        0! = 1
        1! = 1
        2! = 1 x 2
        3! = 1 x 2 x 3
        ...
        """
        return 1 if n < 2 else reduce(lambda x, y: x * y, range(1, n + 1))


    factorials = [factorial(x) for x in range(10)]
    print(factorials)

    # Using built-in arithmetic functions from `operator` module

    print(reduce(lambda x, y: x + y, [2, 3, 4]))
    print(reduce(add, [2, 3, 4]))

    print(reduce(lambda x, y: x * y, [1, 2, 3]))
    print(reduce(mul, [1, 2, 3]))
