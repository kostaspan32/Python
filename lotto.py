from random import seed
from random import randrange
from datetime import datetime #all 3 at the beggining

seed(datetime.now()) #once, before randint call

column = set()

rand_number = randrange(10, 20)
column.add(rand_number)

while True:
    rand_number = randrange (10, 20)
    if rand_number not in column:
        column.add(rand_number)
        break

print(column)
