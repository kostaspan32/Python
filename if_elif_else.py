print("Lets solve an equation ax + b = 0 !")
a = int(input('Please type number a : '))

if a == 0:
    print('')
    print('The equation is invalid')

else:
    print('')
    b = int(input('Please type number b : '))
    x = -b/a
    print('')
    print('The solution is ' + str(x))



