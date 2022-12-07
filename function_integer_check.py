def input_integer():
    while True:
        user_input = input('Please type an integer! : ').strip()

        if user_input.isdigit():
            return int(user_input)

        else:
            print('Only digits please!')


print(input_integer())



input_integer()