"""
https://seddonym.me/2019/08/03/ioc-techniques/
"""


# Polymorphism

class Animal:
    def speak(self):
        raise NotImplementedError


class Cat(Animal):
    def speak(self):
        print("Meow.")


class Dog(Animal):
    def speak(self):
        print("Woof.")


# Duck Typing -- does _NOT_ need to extend base class Animal

class Duck:
    def speak(self):
        print("Quack.")


class Cow:
    def speak(self):
        print("Moo.")


def make_animal_speak(animal):
    """driver method"""
    animal.speak()


if __name__ == '__main__':
    make_animal_speak(Cat())
    make_animal_speak(Dog())

    make_animal_speak(Duck())
    make_animal_speak(Cow())
