def max3(x, y, z):
    if x >= y and x >= z:
        max = x

    elif y >= x and y >= z:
        max = y

    elif z >= x and z >= y:
        max = z

    else:
        max = x

    return max

x = int(input('Give number x: '))
y = int(input('Give number y: '))
z = int(input('Give number z: '))
maximum = max3(x, y, z)

print(f'Max is {maximum}')

for i in range(1, maximum + 1):
    sq = i * i
    print(sq)

