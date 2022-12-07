def print_list(list):
    if len(list) > 0:
        print(list[0], end=' ')
        print_list(list[1:])


def print_list2(list):
    if len(list) > 0:
        print_list2(list[1:])
        print(list[0], end=' ')


list = [1, 2, 3, 4]
print_list(list)
print('')
print_list2(list)
