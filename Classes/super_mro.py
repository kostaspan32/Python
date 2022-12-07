class A:
    def __init__(self):
        print("Entering A")
        super().__init__()
        print("Exiting A")


obj = A()
print('=' * 20)


class B1(A):
    def __init__(self):
        print("Entering B1")
        super().__init__()
        print("Exiting B1")


obj2 = B1()
print('=' * 20)


class B2(A):
    def __init__(self):
        print("Entering B2")
        super().__init__()
        print("Exiting B2")


obj3 = B2()
print('=' * 20)


class D(B1, B2):
    def __init__(self):
        print("Entering D")
        super().__init__()
        print("Exiting D")


obj4 = D()