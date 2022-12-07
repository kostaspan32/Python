from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a = None, point_b = None):
        self.point_a = point_a
        self.point_b = point_b

    def set_point_a(self, x, y):
        self.x = x
        self.y = y
        self.point_a = Point(x, y)

    def set_point_b(self, x, y):
        self.x = x
        self.y = y
        self.point_b = Point(x, y)

    def length(self):
        return sqrt((self.point_a.x - self.point_b.x)**2 + (self.point_a.y - self.point_b.y)**2)


l = Line(Point(1,1), Point(4, 5))
print(l.length())
l.set_point_a(0, 0)
l.set_point_b(0, 0)
print(l.length())




