for a in range(1, 21):
    for b in range (1, 21):
        for c in range(1,21):
            if a**2 + b**2 == c**2:
                print('(' + str(a) + ',' + str(b) + ',' + str(c) + ')')