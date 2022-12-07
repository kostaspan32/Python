def find(x, number_list, position):
    if x == number_list[len(number_list)//2]:
        return f'Position is {position}'

    if len(number_list) <= 2:
        if x not in number_list:
            print(f'{x} not in number list!')
            return -1

    if x > number_list[(len(number_list)-1)//2]:
        number_list = number_list[(len(number_list)//2):]
        position += len(number_list)//2
        return find(x, number_list, position)

    if x < number_list[len(number_list)//2]:
        number_list = number_list[:(len(number_list)//2 + 1)]
        position -= len(number_list)//2
        return find(x, number_list, position)



user_list = [2, 33, 22, 14, 25, 29, 37, 65, 39, 0, 23, 34]
middle = len(user_list)//2
user_list.sort()
number = 22
print(find(number, user_list, middle))