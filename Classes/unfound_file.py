try:
    with open('jsonantigoni.json') as f:
        print(f.read())

except FileNotFoundError:
    print('File not found, do you want to update?')
    user_input = input('Yes or no? : ').strip().lower()
    if user_input == 'yes':
        with open('jsonantigoni.json', 'w') as f:
            f.write('json antigoni')

    else:
        print('KK Bye Bye')

