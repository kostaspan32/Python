from random import seed
from random import randrange
from datetime import datetime

# seed(datetime.now())
#determine hierarchy?
my_list = ['Rock', 'Paper', 'Scissors']
record_list = []



#determine winner
round_count = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

while True:

    user_move = input('Please make your move: ')
    while user_move not in my_list:
        user_move = input('From Rock, Paper, Scissors please: ')

    x = randrange(0, len(my_list))
    pc_move = my_list[x]
    print(f'Pc played {pc_move}')

    round_count += 1

    if user_move + pc_move == 'RockScissors':
        cnt1 += 1
        cnt3 += 1
        print('Rock beats Scissors')

    if user_move + pc_move == 'ScissorsRock':
        cnt2 += 1
        cnt4 += 1
        print('Rock beats Scissors')

    if user_move + pc_move == 'ScissorsPaper':
        cnt1 += 1
        cnt3 += 1
        print('Scissors beats Paper')

    if user_move + pc_move == 'PaperScissors':
        cnt2 += 1
        cnt4 += 1
        print('Scissors beats Paper')

    if user_move + pc_move == 'PaperRock':
        cnt1 += 1
        cnt3 += 1
        print('Paper beats Rock')

    if user_move + pc_move == 'RockPaper':
        cnt2 += 1
        cnt4 += 1
        print('Paper beats Rock')

    # print winner
    if cnt1 == cnt2:
        print(f'Round {round_count} is a draw!')
        record_list.append(f'Round {round_count} is a draw!')

    if cnt1 > cnt2:
        print(f'Round {round_count} won by player!')
        record_list.append(f'Round {round_count} won by player!')

    if cnt2 > cnt1:
        print(f'Round {round_count} won by pc!')
        record_list.append(f'Round {round_count} won by pc!')

    print(f'Score is: Player {cnt3} - PC {cnt4}')
    cnt1 = 0
    cnt2 = 0

    if cnt3 == 3:
        print(f'Player won the game! Score: {cnt3} - {cnt4}')
        break

    if cnt4 == 3:
        print(f'PC won the game! Score: {cnt3} - {cnt4}')
        break

print(record_list)


