user_input = input('Give an integer: ')

while True:
    if user_input.isdigit():
        number = int(user_input)
        print(f'Number entered is {number}')
        break

    else:
        user_input = input('Give an INTEGER please: ')

print(f'other number is {1/4:.2}')
