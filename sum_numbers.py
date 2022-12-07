print('Give 10 numbers so that we sum them up')
my_list = []
s = 0
cnt = 0

while len(my_list) < 10:
    user_input = int(input('Please give a number: '))
    my_list.append(user_input)
    s += my_list[cnt]
    cnt += 1

print(s)