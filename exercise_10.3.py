def f(arg):
    print(f'id: {id(arg)}')
    print(arg)
    arg = [3]
    print(f'id: {id(arg)}')
    print(arg)

l = [1, 2]
print(f'id: {id(l)}')
f(l)
print(f'id: {id(l)}')
print(l)