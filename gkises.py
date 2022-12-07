x = int(input('Give x: '))

y = int(input('Give y: '))

z = int(input('Give z: '))

if x >= y and x >= z:
    print('The bigger number is ' + str(x))

elif y >= x and y >= z:
    print('The bigger number is ' + str(y))

else:
    print('The bigger number is ' + str(z))
