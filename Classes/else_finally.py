def safe_divide():
    try:
        x = int(input('Give nominator : '))
        y = int(input('Give denominator : '))
        res = x / y

    except ZeroDivisionError:
        print('Error, division by zero!')

    except Exception as e:
        print(f'Something went really wrong : {e}')

    else:
        return res

    finally:
        return None

print(safe_divide())