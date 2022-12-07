from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

counter = {}

for i in range(1, 6+1):
    counter[i] = 0

print(counter)

N = 10

for cnt in range(N):
    x = randrange(1, 7)
    counter[x] += 1

print(counter)

for key, value in counter.items():
    print('Percentage for ' + str(key) + ' is ' + str(value/N))

print(max(counter.values()))
