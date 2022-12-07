from abc import ABC, abstractmethod

class GeometricObjectInterface(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(GeometricObjectInterface):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * 3.14

    def area(self):
        return 3.14 * self.radius ** 2


class Resizable(ABC):
    @abstractmethod
    def resize(self):
        pass


class ResizableCircle(Circle, Resizable):
    def __init__(self, radius):
        Circle.__init__(self , radius)

    def resize(self, new_radius):
        self.radius = new_radius


