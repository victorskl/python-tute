"""
Abstract Base Classes
https://docs.python.org/3/library/abc.html
"""
from abc import ABC, abstractmethod


class RealAbc(ABC):

    def __init__(self):
        self.some_value = "real"

    @abstractmethod
    def must_impl(self):
        raise NotImplementedError


class RealChild(RealAbc):

    def must_impl(self):
        print(self.some_value)


class MyAbc(ABC):
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)


class MyHelper(MyAbc):

    def __init__(self, value, overload):
        super().__init__(value)
        self.overload = overload

    def with_overload(self):
        print(f"{self.value} {self.overload}")


if __name__ == '__main__':
    my = MyAbc(value="hi")
    print(my.value)
    my.show()

    child = MyHelper(value="hi", overload="joe")
    child.show()
    child.with_overload()

    real_child = RealChild()
    real_child.must_impl()

    try:
        real = RealAbc()
    except TypeError as e:
        print(e)
