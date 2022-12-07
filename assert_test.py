l = [1, 2, 3]


def su(sth):
    s = 0
    for item in sth:
        s += item
    return s


assert su(l) != 6