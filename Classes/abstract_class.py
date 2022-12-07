from abc import ABC, abstractmethod #abc = Abstract Based Class


class MyAbstractClass(ABC):
    def __init__(self, attr):
        self.attr = attr

    @abstractmethod
    def my_abstract_method(self):
        pass


obj = MyAbstractClass(1)