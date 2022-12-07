class Point3D:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.counter = 0
        self.ar = [x, y, z]

    def __str__(self):
        return f'Point {self.name} is ({self.x},{self.y},{self.z}, counter is {self.counter})'

    def __pos__(self):
        self.counter += 1

    def __neg__(self):
        self.counter -= 1

    def __add__(self, other):
        if isinstance(other, Point3D):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Point3D(input('Please type point name: '), new_x, new_y, new_z)
        else:
            return None

    def __iadd__(self, other):
        if isinstance(other, Point3D):
            self.x = self.x + other.x
            self.y = self.y + other.y
            self.z = self.z + other.z
            return self

    def __len__(self):
        return len(self.ar)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            return 0

    def __setitem__(self, item, val):
        if item == 0:
            self.x = val
        elif item == 1:
            self.y = val
        elif item == 2:
            self.z = val
        else:
            return 0


a = Point3D('a', 1, 1, 1)
b = Point3D('b', 2, 2, 2)
c = a + b
print(c)
print(a)
a = a + b
print(a)
a = a + b
print(a)
+a
+a
+a
print(a)
-a
-a
print(a)
print(a[1])