my_list = [1, 3, 4, 20, 0, 100, 29, 234, 54, 21]
cnt = 0
maximum = 0

while cnt < len(my_list):
    if maximum < my_list[cnt]:
        maximum = my_list[cnt]

    cnt += 1

print(maximum)


