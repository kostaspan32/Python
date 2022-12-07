def float_average(*floats):
    cnt = 0
    s = 0
    for number in floats:
        cnt += 1
        s += number
    print(f" s = {s} cnt = {cnt}")
    return s / cnt

print(f' float average = {float_average(1, 2, 3,4 , 4, 5)}')
