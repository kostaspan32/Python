def input_float():
    while True:

        user_input = input('Please type a float! : ').strip()
        user_input_list = list(user_input)
        if '.' in user_input_list:

            if user_input_list.count('.') > 1:
                print('Only one dot please! ')
                continue

            if len(user_input_list) >= 3:
                if user_input[:user_input_list.index('.')].isdigit() and user_input[user_input_list.index('.')] == '.' and user_input[(user_input_list.index('.') + 1):].isdigit():
                    return float(user_input)

        else:
            if user_input.strip().isdigit():
                return float(user_input)
            print('A float please! ')

print(input_float())