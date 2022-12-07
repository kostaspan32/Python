def f(x, y, z):
    return 2 * x**3 + 3 * x**2 * y + y**2 * z + 1

print(f(5, 2, 3))
print(f(5, y=2, z=3))
print(f(5, 2, z=3))
print(f(x=5, y=2, z=3))