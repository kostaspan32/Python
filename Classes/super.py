class Base:
    def __init__(self, b_attr):
        self.b_attr = b_attr

    def __str__(self):
        return "Some info about base class"


class Derived(Base):
    def __init__(self, b_attr, d_attr):
        super().__init__(b_attr)
        self.d_attr = d_attr

    def __str__(self):
        return "Some info about derived class"

    def giga_info(self):
        return super().__str__() + ' AND ' + self.__str__()

d = Derived(1, 2)
print(d)
print(d.giga_info())