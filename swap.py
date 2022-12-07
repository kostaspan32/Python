def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = 3
b = 4
print(f' a = {a} , b = {b}')
a, b = swap(a, b)
print(f' a = {a} , b = {b}')
a, b = b, a
print(f' a = {a} , b = {b}')