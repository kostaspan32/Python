while True:
    try:
        x = input("Give nonnegative integer: ")
        if not x.isdigit():
            raise ValueError('Only digits please!')
        if x == '':
            raise ValueError("No digits found")
        if int(x) < 0:
            raise ValueError("NonNegative Value entered")
    except ValueError as v:
        print(v)

    except Exception as e:
        print(e)
    else:
        print(x)
        break