def students(*args, **kwargs):
    s = 0
    for number in args:
        s += number

    average = s / len(args)
    print(average)
    dictionary = {}
    for key, value in kwargs.items():
        if value in dictionary:
            dictionary[value] += [key]

        else:
            dictionary[value] = [key]
    print(dictionary)

students(5, 4, 3, Banner = 'Discrete Mathematics', Kane = 'Discrete Mathematics', Stark = 'Programming')