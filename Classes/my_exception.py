class MyException(Exception):
    def __init__(self, val, message):
        self.val = val
        self.message = message

    def __str__(self):
        print(self.message)


while True:
    try:
        x = input("Give nonnegative integer: ")
        if int(x) < 0:
            raise MyException(x, f'Value {x} imported is negative!')

        if int(x) < 100:
            raise MyException(x, f'ValueTooSmallError: {x} is < 100')

        if int(x) > 200:
            raise MyException(x, f'ValueTooLargeError: {x} is > 200')

        if int(x) % 5 != 0:
            raise MyException(x, f'NotMultipleOfFiveError: {x} is not multiplicative of 5')

    except MyException as e:
        print(e)

    except Exception as e:
        print(e)
