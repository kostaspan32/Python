hidden_list = [1, 3, 2, 2, 4, 1, 4, 3]
user_list = []
cnt = 0
game_attempts = 0
high_score = 300.000

for number in hidden_list:
    user_list.append('closed')

while game_attempts >= 0:

    for i in range(int(len(hidden_list) / 2)):
        print('Please pick two cards from the following list')
        print(user_list)

        card1 = int(input('Please type the position of the first card: '))

        while card1 < 1 or card1 >8 :
            print('Between 1 and 8 please!')
            card1 = int(input('Please type the position of the first card: '))

        while user_list[card1 - 1] != 'closed':
            print('Please pick a closed card: ')
            card1 = int(input('Please type the position of the first card: '))

        print(hidden_list[card1 - 1])

        card2 = int(input('Please type the position the second card: '))
        while card2 < 1 or card2 > 8:
            print('Between 1 and 8 please!')
            card12= int(input('Please type the position of the first card: '))

        while int(card2) == int(card1):
            print('You picked the same card. Please pick another card!')
            card2 = int(input('Please type the position the second card: '))

        while user_list[card2 - 1] != 'closed':
            print('Please pick a closed card: ')
            card2 = int(input('Please type the position the second card: '))

        print(hidden_list[card2 - 1])

        while hidden_list[card1 - 1] != hidden_list[card2 - 1]:
            print('You failed, try again!')
            cnt += 1

            print(user_list)

            card1 = int(input('Please type the position of the first card: '))
            while card1 < 1 or card1 > 8:
                print('Between 1 and 8 please!')
                card1 = int(input('Please type the position of the first card: '))

            while user_list[card1 - 1] != 'closed':
                print('Please pick a closed card: ')
                card1 = int(input('Please type the position of the first card: '))

            print(hidden_list[card1 - 1])

            card2 = int(input('Please type the position the second card: '))
            while card2 < 1 or card1 > 8:
                print('Between 1 and 8 please!')
                card2 = int(input('Please type the position of the first card: '))

            while int(card2) == int(card1):
                print('You picked the same card. Please pick another card!')
                card2 = int(input('Please type the position the second card: '))

            while user_list[card2 - 1] != 'closed':
                print('Please pick a closed card: ')
                card2 = int(input('Please type the position the second card: '))

            print(hidden_list[card2 - 1])

        if hidden_list[card1 - 1] == hidden_list[card2 - 1]:
            print('Well done, down two cards!')
            cnt += 1
            user_list[card1 - 1] = str(hidden_list[card1 - 1])
            user_list[card2 - 1] = str(hidden_list[card2 - 1])

        if i == 3:
            print('You won in ' + str(cnt) + ' attempts')
            if cnt < high_score:
                high_score = cnt
            print('Your high score is ' + str(high_score))

            print(user_list)
            answer = input('Would you like to play again? : ')
            if answer == 'Yes':
                game_attempts += 1
                cnt = 0
                user_list.clear()
                user_list = ['closed', 'closed', 'closed', 'closed', 'closed', 'closed', 'closed', 'closed']

            else:
                print('Well okay then, bye bye!')
                game_attempts = -1



