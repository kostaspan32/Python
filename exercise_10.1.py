def f(arg):
    print(arg)
    arg = 'Change'
    print(f'id: {id(arg)} ')
    print(arg)

s = 'Initial'
print(f'id: {id(s)} ')
f(s)
print(f'id: {id(s)} ')
print(s)