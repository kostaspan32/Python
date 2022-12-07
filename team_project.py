from typing import Set, Any

mathematics = set()
geography = set()
N = 20
classroom = set()

for number in range(1, N+1):
    classroom.add(number)

from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

cnt1 = 0
for i in range(N):

    x = randrange(1, N+1)

    if x not in mathematics:
        cnt1 += 1
        mathematics.add(x)
        if cnt1 == N / 2:
            break


geography = classroom - mathematics

print("Mathematics group is" + str(mathematics))
print("Geography group is " + str(geography))
print("Classroom is " + str(classroom))

pair_list = []

for empty_pair in range(0, 10):
    pair_list.append([])

cnt3 = 0

for student1 in mathematics:

    pair_list[cnt3].append(student1)
    cnt3 += 1

for student2 in geography:
    p = randrange(0, N//2)
        print(pair_list[p])
            cnt3 += 1

        else:
            pair_list[p].append(student2)



print('Pairs are ' + str(pair_list))







