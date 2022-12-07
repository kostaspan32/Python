def mkd(x, y):
    if x == y:
        return x

    while x != y:
        if x > y:
            x = x - y

        else:
            y = y - x

    return x

number1 = 90
number2 = 1200330
print(f'MKD({number1}, {number2}) = {mkd(number1, number2)}')

