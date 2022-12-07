my_list = [[1, 23, 32, 0], [41, 54, 12, 66], [18, 21, 0, 45]]

for row in my_list:
    for element in row:
        print(element, end=' ')

    print('')

my_list.insert(0, [0, 0, 0, 0])

for row in my_list:
    for element in row:
        print(element, end=' ')

    print('')

for row in my_list:
    row.append(1)

for row in my_list:
    for element in row:
        print(element, end=' ')

    print('')
