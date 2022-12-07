class C:
    counter = 0
    def __init__(self):
        C.counter += 1

oj1 = C()
oj2 = C()
print(C.counter, oj1.counter, oj2.counter)