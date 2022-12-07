def sorting(l):
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] < l[j]:
                x = l.pop(i)
                l.insert(j, x)

    return(l)


number_list = [2, 9, 3, 5, 4, 6, 0, 8, 1, 7]
print(sorting(number_list))