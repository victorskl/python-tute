"""
https://realpython.com/python-kwargs-and-args/
"""


def first(**kwargs):
    return kwargs.get('key')


def second(**kwargs):
    first(**kwargs)


class Parent:
    def first(self, **kwargs):
        return kwargs.get('key')


class Child(Parent):
    def second(self, **kwargs):
        return self.first(**kwargs)


def my_sum(a, b, c):
    return a + b + c


def sum_all(*args):
    result = 0
    for x in args:
        result += x
    return result


def merge_list(list1, list2):
    return [*list1, *list2]


def merge_dict(dict1, dict2):
    return {**dict1, **dict2}


if __name__ == '__main__':
    for i in range(2):
        print(first(key=i))

    print(second(key='second'))  # None it's already unpacked within second() function, so it won't carry into first()

    print(Child().second(key='second'))  # but within class hierarchy scope, you can pass around

    # ---

    my_list_1 = [1, 2, 3]
    my_list_2 = [4, 5]
    my_list_3 = [6, 7, 8, 9]

    my_dict1 = {'A': 1, 'B': 2}
    my_dict2 = {'C': 3, 'D': 4}

    my_str = "RealPython"

    print(my_sum(*my_list_1))

    print(sum_all(*my_list_1, *my_list_2, *my_list_3))

    print(merge_list(my_list_1, my_list_2))

    print(my_list_1 + my_list_2)  # but using + operator is even more intuitive

    print(merge_dict(my_dict1, my_dict2))

    x = [*my_str]  # string is iterable list of characters, so we can explode the string into the char list
    print(x)

    *y, = my_str  # `y,` is tuple unpacking that ends up `y` list; then unpack `y` list with *
    print(y)
