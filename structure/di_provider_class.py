"""
https://stackoverflow.com/questions/940564/how-does-spring-for-python-compare-with-spring-for-java
"""
from abc import ABC, abstractmethod


class AbstractProvider(ABC):

    @abstractmethod
    def get_greeting(self, who):
        pass


# A concrete class implementing the greeting provider interface
class EnglishGreetingProvider(AbstractProvider):
    _greeting = "Hello %s!"

    def get_greeting(self, who):
        return self._greeting % who


# Alternative implementation
class FrenchGreetingProvider(AbstractProvider):
    _greeting = "Bonjour %s!"

    def get_greeting(self, who):
        return self._greeting % who


# A class that takes a greeting provider factory as a parameter
class ConsoleGreeter(object):
    def __init__(self, who, provider=AbstractProvider):
        self.who = who
        self.provider = provider()

    def greet(self):
        print(self.provider.get_greeting(self.who))


if __name__ == '__main__':
    # Default wiring
    greeter = ConsoleGreeter(who="World", provider=EnglishGreetingProvider)
    greeter.greet()

    greeter = ConsoleGreeter(who="World", provider=FrenchGreetingProvider)
    greeter.greet()
