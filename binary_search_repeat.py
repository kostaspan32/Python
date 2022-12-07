def find(array, x):
    start = 0
    finish = len(array) - 1
    middle = (start + finish) // 2

    while True:
        middle = (start + finish) // 2
        if finish - start <= 2:
            if x not in array[start:finish + 1]:
                return -1

        if x == array[middle]:
            return middle

        elif x > array[middle]:
            start = middle + 1

        elif x < array[middle]:
            finish = middle - 1


my_list = [i*i for i in range(10)]
number = 25
print(find(my_list, number))