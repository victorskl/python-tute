"""
a fluent interface or method chaining

https://www.google.com/search?q=python+fluent+api
"""


class Classic(object):
    """
    For basic about Python OOP, Class and Object, see
    https://docs.python.org/3/tutorial/classes.html
    https://realpython.com/python-property/
    """

    def __init__(self):
        super().__init__()
        self._name = None
        self._address = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def __str__(self):
        return f"name: {self._name}, address: {self._address}"


class FluentApi(object):

    def __init__(self):
        self._address = None
        self._name = None

    def name(self, name):
        self._name = name
        return self

    def address(self, address):
        self._address = address
        return self

    def __str__(self):
        return f"name: {self._name}, address: {self._address}"


if __name__ == '__main__':
    obj = Classic()
    obj.name = 'John Doe'
    obj.address = '1 Old Way Drive, VIC 3131'

    print(obj)
    print(type(obj))
    print(dir(obj))

    # ---

    fluent = (
        FluentApi()
        .name("Mickey Doe")
        .address("1 New Way Drive, VIC 3054")
    )
    print(fluent)
    print(type(fluent))
    print(dir(fluent))
