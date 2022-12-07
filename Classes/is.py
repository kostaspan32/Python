l1 = [1, 2]
l2 = [1, 2]
l3 = l2 # PROSTHETW tropo anaforas, dhladh allages se l3 tha allaksoun kai to l2 vice versa
print(l1 is l2)
print(l1 == l2)
l3.append(1)
print(l2)
print('=' * 20)

class C:
    def __init__(self, x):
        self.x = x

o1 = C(1)
o2 = C(1)
o3 = o2
print(id(o1), id(o2), id(o3))
print(o1 is o2)
print(o1 == o2)
print(o3 is o2)
print('=' * 20)

print(isinstance(l1, list))
print(isinstance(1, (list, int)))
print(isinstance(o1, C))
