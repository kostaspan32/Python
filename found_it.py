numbers = [11, 23, 15, 29, 30, 5, 2, 3]

search = 2
cnt = 0

for number in numbers:
    cnt += 1
    if number == search:
        print('Found it! It is the ' + str(cnt) + 'th number!')
        break
else:
    print('Didn"t find it!')

