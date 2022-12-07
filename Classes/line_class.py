from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'


class Line:
    def __init__(self):
        self.point_a = (0, 0)
        self.point_b = (0, 0)
        self.length = 0

    def set_points(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def measure(self):
        self.length = sqrt((self.point_a.x - self.point_b.x)**2 + (self.point_a.y - self.point_b.y)**2)
        return self.length

    def __str__(self):
        return f'Point A is {self.point_a}, Point B is {self.point_b}, line length is {self.measure()}'

    def __ge__(self, other):
        if isinstance(other, Line):
            return self.measure() >= other.measure()

        elif isinstance(other, int):
            return self.measure() >= other

    def __gt__(self, other):
        if isinstance(other, Line):
            return self.measure() > other.measure()
        elif isinstance(other, int):
            return self.measure() > other

    def __eq__(self, other):
        if isinstance(other, Line):
            return self.measure() == other.measure()

        elif isinstance(other, int):
            return self.measure() == other


zero_line = Line()
my_line = Line()
my_line.set_points(Point(1, 1), Point(4, 5))
your_line = Line()
your_line.set_points(Point(1,1), Point(4, 8))
print(my_line.measure())
print(my_line)
print(f'{my_line > 6}')
print(my_line > your_line)


