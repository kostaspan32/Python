my_list = []
cnt = 0
user_input = int(input('Please type ten numbers between 10 and 20: '))

while user_input < 10 or user_input > 20:
    user_input = int(input('Between 10 and 20 please: '))

while 10 <= user_input <= 20:
    cnt += 1
    my_list.append(user_input)
    if cnt == 10:
        break
    user_input = int(input('Type the ' + str(cnt+1) + 'th number please: '))

    while user_input < 10 or user_input > 20:
        user_input = int(input('Between 10 and 20 please: '))


print(my_list)
my_tuple = tuple(my_list)

list_squares = []

for i in range(10):
    list_squares.append(my_list[i]**2)

print(list_squares)



