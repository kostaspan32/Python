def is_odd(number):
    return number % 2 == 1



def is_even(number):
    return number % 2 == 0



def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


def is_square(number):

    sq = 0
    i = 0
    while sq < number:
        i += 1
        sq = i ** 2

    return sq == number


def is_cube(number):

    cu = 0
    i = 0
    while cu < number:
        i += 1
        cu = i ** 3

    return cu == number


for number in range(1, 100 + 1):
    print(str(number) + ' is', end=' ')
    if is_odd(number):
        print('odd,', end=' ')
    if is_even(number):
        print('even,', end=' ')
    if is_prime(number):
        print('prime,', end=' ')
    if is_square(number):
        print('square,', end=' ')
    if is_cube(number):
        print('cube,', end=' ')
    print('')
