try:
    x = int(input('Give nominator : '))
    y = int(input('Give denominator : '))
    res = x / y
    print(f"Result is {res}!")

except ZeroDivisionError:
    print('Error, division by zero!')