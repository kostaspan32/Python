def f():
    global x
    x = 3
    print(x)


x = 2
f()
print(x)
print('======================')


def f():
    global x
    x = 3
    print(x)


f()
x = 2
print(x)
print('==================')

def f():
    global x
    print(x)


x = 2
f()
print(x)
