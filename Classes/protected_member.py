class Base:
    def __init__(self):
        self.__b_attr = 0
        self._d_attr = 0


class Derived(Base):
    def __init__(self):
        super().__init__()
        print(self._Base__b_attr) #how to access "private" member
        print(self._d_attr) #protected member always accesible, simply agree to not use


d = Derived()


