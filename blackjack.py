from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

player_win_count = 0
computer_win_count = 0

def main():

    global player_win_count
    global computer_win_count
    player_blackjack = 0
    computer_blackjack = 0
    cnt = 0
    cntc = 0
    #create deck
    kind = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    shape = ['club', 'spades', 'heart', 'diamond']

    deck = [(k, s) for k in kind for s in shape]

    player = []
    computer = []

    #player_move
    print('Player turn!')
    for i in range(2):
        player.insert(0, deck.pop(randrange(len(deck))))
        print(f'Card drawn: {player[0]}')
        if (player[cnt])[0] == 'jack' or (player[cnt])[0] == 'queen' or (player[cnt])[0] == 'king':
            player_blackjack += 10
        elif (player[cnt])[0] == 'ace':
            ace_input = int(input('Do you want it as a 1 or as an 11? : '))
            while ace_input not in (1, 11):
                ace_input = int(input('1 or 11 please : '))
            player_blackjack += ace_input
        else:
            player_blackjack += (player[cnt])[0]

    print(f'Player blackjack: {player_blackjack}')

    if player_blackjack == 21:
        print('You reached 21, you won!')
        print(f'Cards: {player}')
        player_win_count += 1

    while player_blackjack < 21:

            user_input = input('Do you wish to draw another card? : ').strip().lower()
            if user_input == 'yes':
                player.insert(0, deck.pop(randrange(len(deck))))
                print(f'Card drawn: {player[0]}')
                if (player[cnt])[0] == 'jack' or (player[cnt])[0] == 'queen' or (player[cnt])[0] == 'king':
                    player_blackjack += 10
                elif (player[cnt])[0] == 'ace':
                    ace_input = int(input('Do you want it as a 1 or as an 11? : '))
                    while ace_input not in (1, 11):
                        ace_input = int(input('1 or 11 please : '))
                    player_blackjack += ace_input
                else:
                    player_blackjack += (player[cnt])[0]
                print(f'Player blackjack: {player_blackjack}')
                cnt += 1
                if player_blackjack == 21:
                    print('You reached 21, you won!')
                    print(f'Cards: {player}')
                    player_win_count += 1
                    break
                if player_blackjack > 21:
                    print('You lost')
                    print(f'Cards: {player}')
                    computer_win_count += 1
                    break
            if user_input == 'no':
                print(f'Well enough! Your score is {player_blackjack}')
                print(f'Cards: {player}')
                break


    print('================================')

    #computer_move
    print('Computer turn!')
    while computer_blackjack < 21 and player_blackjack < 21:
        computer.insert(0, deck.pop(randrange(len(deck))))
        print(f'Card drawn: {computer[0]}')
        if (computer[cntc])[0] == 'jack' or (computer[cntc])[0] == 'queen' or (computer[cntc])[0] == 'king':
            computer_blackjack += 10
        elif (computer[cntc])[0] == 'ace':
            ace_input = int(input('Do you want it as a 1 or as an 11? : '))
            while ace_input not in (1, 11):
                ace_input = int(input('1 or 11 please : '))
            computer_blackjack += ace_input
        else:
            computer_blackjack += (computer[cntc])[0]
        print(f'Computer blackjack: {computer_blackjack}')
        cnt += 1
        if computer_blackjack > 21:
            print('Computer lost')
            print(f'Cards: {computer}')
            player_win_count += 1
            break
        if computer_blackjack >= player_blackjack:
            print('Computer won!')
            print(f'Cards: {computer}')
            computer_win_count += 1
            break


main()
print(f'Player: {player_win_count} - Computer: {computer_win_count}')
while input('Do you want to play again? :  ').strip().lower() == 'yes':
    main()
    print(f'Player: {player_win_count} - Computer: {computer_win_count}')

print('Bye Bye!')

