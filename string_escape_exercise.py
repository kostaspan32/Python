from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

table = []

for row in range(3):

    for _ in range(3):
        print('+----', end='')

    print('+')

    for column in range(3):

        x = randrange(0, 1000)
        print(('|' + str(x) + '\t').expandtabs(5), end='')
    print('|')

for _ in range(3):
    print('+----', end='')










