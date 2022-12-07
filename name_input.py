while True:

    string = input('Please enter name: ')
    string = string.strip()

    if string.isalpha():
        name = string.capitalize()
        print(f"Name entered: {name}")
        break

    else:
        print("Only characters please!")



