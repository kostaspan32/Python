l = [1, 2, 3]
del l[1]
print(l)

d = {1:1, 2:2}
del d[1]
print(d)

class C:
    c = 0
    def __init__(self):
        C.c += 1

    def __del__(self):
        C.c -= 1


oj1 = C()
oj2 = C()
print(C.c)
del oj1
print(C.c)