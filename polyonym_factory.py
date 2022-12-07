def polyonym_factory(a, b, c):
    def f(x):
        return a * x ** 2 + b * x + c
    return f

function = polyonym_factory(1, 4, 4)
print(function(1))