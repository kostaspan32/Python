def f(arg):
    print(arg)
    arg.append(3)
    print(arg)


l = [1, 2]
f(l)
print(l)