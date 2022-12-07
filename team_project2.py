from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

classroom = set()
N = 20
mathematics_set = set()
geography_set = set()

# make set --> list

pupils = list(classroom)
# insert pupils
for pupil in range(N):
    pupils.append("pupil" + str(pupil))

print('Pupils are ' + str(pupils))

for repeat in range(N//2):
    position1 = randrange(len(pupils))
    first = pupils.pop(position1)
    position2 = randrange(len(pupils))
    second = pupils.pop(position2)
    team = (first, second)
    mathematics_set.add(team)

for pupil in range(N):
    pupils.append("pupil" + str(pupil))

for repeat in range(N // 2):
    position1 = randrange(len(pupils))
    first = pupils.pop(position1)
    position2 = randrange(len(pupils))
    second = pupils.pop(position2)
    team = (first, second)
    geography_set.add(team)

print('Maths teams are ' + str(mathematics_set))
print('Geography teams are ' + str(geography_set))

