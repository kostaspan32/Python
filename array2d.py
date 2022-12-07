my_list = [
    [1, 2, 3],
    [4, 5, 6]
]

print(my_list[0][1])

my_list = []

rows = int(input('Give number of rows: '))
cols = int(input('Give number of columns: '))

for i in range(rows):
    my_list.append([])
    for j in range(cols):
        element = int(input('Give ' + str(i) + ',' + str(j) + ' element: '))
        my_list[i].append(element)

for row in my_list:
    for element in row:
        print(element, end=' ')
    print('')





