user_input = input("Please type a number so that we print its square: ")

while user_input != 'quit':

        print('You did not enter a number!')
        user_input = input("Please type a number so that we print its square: ")

    else:
        print(int(user_input)**2)
        user_input = input("Please type another number so that we print its square: ")


else:
    print('Bye bye!')

