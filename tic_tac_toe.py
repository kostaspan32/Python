from random import randrange

list0 = ['+--------+--------+--------+']
list1 = ['|', '', '|', '', '|', '', '|']
list2 = ['+--------+--------+--------+']
list3 = ['|', '', '|', '', '|', '', '|']
list4 = ['+--------+--------+--------+']
list5 = ['|', '', '|', '', '|', '', '|']
list6 = ['+--------+--------+--------+']

def print_board():
    print(list0)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    print(list6)

def winner_check(rival1, rival2):
    if list1[1] == list1[3] == list1[5] == 'O':
        print(f'{rival1} won!')
        return 1
    if list1[1] == list1[3] == list1[5] == 'X':
        print(f'{rival2} won!')
        return 2

    if list3[1] == list3[3] == list3[5] == 'O':
        print(f'{rival1} won!')
        return 1

    if list3[1] == list3[3] == list3[5] == 'X':
        print(f'{rival2} won!')
        return 2

    if list5[1] == list5[3] == list5[5] == 'O':
        print(f'{rival1} won!')
        return 1

    if list5[1] == list5[3] == list5[5] == 'X':
        print(f'{rival2} won!')
        return 2

    if list1[1] == list3[1] == list5[1] == 'O':
        print(f'{rival1} won!')
        return 1

    if list1[1] == list3[1] == list5[1] == 'X':
        print(f'{rival2} won!')
        return 2

    if list1[3] == list3[3] == list5[3] == 'O':
        print(f'{rival1} won!')
        return 1

    if list1[3] == list3[3] == list5[3] == 'X':
        print(f'{rival2} won!')
        return 2

    if list1[5] == list3[5] == list5[5] == 'O':
        print(f'{rival1} won!')
        return 1

    if list1[5] == list3[5] == list5[5] == 'X':
        print(f'{rival2} won!')
        return 2

    if list1[1] == list3[3] == list5[5] == 'O':
        print(f'{rival1} won!')
        return 1

    if list1[1] == list3[3] == list5[5] == 'X':
        print(f'{rival2} won!')
        return 2

    if list5[1] == list3[3] == list1[5] == 'O':
        print(f'{rival1} won!')
        return 1

    if list5[1] == list3[3] == list1[5] == 'X':
        print(f'{rival2} won!')
        return 2
    if cnt == 9:
        print('Draw')
        return 0

def play(player):
    if position == 1:
        list1.pop(1)
        list1.insert(1, f'{player}')

    if position == 2:
        list1.pop(3)
        list1.insert(3, f'{player}')

    if position == 3:
        list1.pop(5)
        list1.insert(5, f'{player}')

    if position == 4:
        list3.pop(1)
        list3.insert(1, f'{player}')

    if position == 5:
        list3.pop(3)
        list3.insert(3, f'{player}')

    if position == 6:
        list3.pop(5)
        list3.insert(5, f'{player}')

    if position == 7:
        list5.pop(1)
        list5.insert(1, f'{player}')

    if position == 8:
        list5.pop(3)
        list5.insert(3, f'{player}')

    if position == 9:
        list5.pop(5)
        list5.insert(5, f'{player}')

print_board()
opponent = input('Do you want to play vs computer or player? : ').strip().lower()

while opponent != 'player' and opponent != 'computer':
    opponent = input('Please type computer or player : ').strip().lower()

if opponent == 'player':

    print('Whoever plays first has O!')
    played_list = []
    cnt = 0
    for i in range(5):
        cnt += 1

        player1position = int(input('Please type the position of your choice (1-9): '))
        while player1position in played_list:
            player1position = int(input('This position is not empty, pick another: '))

        while player1position > 9 or player1position < 1:
            player1position = int(input('Between 1 and 9 please: '))

        played_list.append(player1position)
        position = player1position

        play('O')
        print_board()
        a = winner_check('Player 1', 'Player 2')
        if a == 0 or a == 1 or a == 2:
            break

        cnt += 1
        player2position = int(input('Please type the position of your choice, different from player 1 (1-9): '))
        while player2position in played_list:
            player2position = int(input('This position is not empty, pick another: '))

        while player2position == player1position:
            player2position = input('Different from player 1 please: ')

        while player2position > 9 or player1position < 1:
            player2position = int(input('Between 1 and 9 please: '))

        position = player2position

        play('X')
        print_board()
        a = winner_check('Player 1', 'Player 2')
        if a == 0 or a == 1 or a == 2:
            break

elif opponent == 'computer':
    cnt = 0
    played_list = []
    not_played_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    level = int(input('Do you want level 1 or level 2? : '))
    while level != 1 and level != 2:
        level = input('1 or 2? : ')

    if level == 1:
        turn = randrange(2)
        for i in range(5):
            cnt += 1
            playerposition = int(input('Please type the position of your choice (1-9): '))
            while playerposition in played_list:
                playerposition = int(input('This position is not empty, pick another: '))

            while playerposition > 9 or playerposition < 1:
                playerposition = int(input('Between 1 and 9 please: '))

            not_played_list.remove(playerposition)
            played_list.append(playerposition)
            position = playerposition

            play('O')
            print_board()
            a = winner_check('Player', 'Computer')
            if a == 0 or a == 1 or a == 2:
                break

            computerposition = not_played_list[randrange(len(not_played_list))]
            played_list.append(computerposition)
            not_played_list.remove(computerposition)
            position = computerposition

            play('X')
            print_board()
            a = winner_check('Player', 'Computer')
            if a == 0 or a == 1 or a == 2:
                break


    if level == 2:
        turn = randrange(2)
        for i in range(5):
            cnt += 1
            playerposition = int(input('Please type the position of your choice (1-9): '))
            while playerposition in played_list:
                playerposition = int(input('This position is not empty, pick another: '))

            while playerposition > 9 or playerposition < 1:
                playerposition = int(input('Between 1 and 9 please: '))

            not_played_list.remove(playerposition)
            played_list.append(playerposition)
            position = playerposition

            play('O')
            print_board()
            a = winner_check('Player', 'Computer')
            if a == 0 or a == 1 or a == 2:
                break
            danger_cnt = 0
            danger_cnt2 = 0
            danger_cnt3 = 0
            if list1[1] == list1[3] == 'O' or list5[1] == list3[3] == 'O' or list5[5] == list3[5] == 'O' and 3 in not_played_list:
                computerposition = 3
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list1[3] == list1[5] == 'O' or list5[5] == list3[3] == 'O' or list5[1] == list3[1] == 'O' and 1 in not_played_list:
                computerposition = 1
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list1[1] == list1[5] == 'O' or list5[3] == list3[3] == 'O' and 2 in not_played_list:
                computerposition = 2
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list3[3] == list3[5] == 'O' or list5[1] == list1[1] == 'O' and 4 in not_played_list:
                computerposition = 4
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list3[1] == list3[5] == 'O' or list5[1] == list1[5] == 'O' or list5[5] == list1[1] == 'O' or list5[3] == list1[3] == 'O' and 5 in not_played_list:
                computerposition = 5
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list1[5] == list5[5] == 'O' or list3[1] == list3[3] == 'O' and 6 in not_played_list:
                computerposition = 6
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list1[1] == list3[1] == 'O' or list5[3] == list5[5] == 'O' or list3[3] == list1[5] == 'O' and 7 in not_played_list:
                computerposition = 7
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list1[3] == list3[3] == 'O' or list5[1] == list5[5] == 'O' and 8 in not_played_list:
                computerposition = 8
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if list1[5] == list3[5] == 'O' or list1[1] == list3[3] == 'O' or list5[3] == list5[1] == 'O' and 9 in not_played_list:
                computerposition = 9
                danger_cnt += 1
                danger_cnt2 += 1
                danger_cnt3 += 1

            if danger_cnt == 0:
                if 5 in not_played_list:
                    danger_cnt2 += 1
                    danger_cnt3 += 1
                    computerposition = 5

            if danger_cnt2 == 0:
                danger_cnt3 += 1
                x = randrange(2, 9, 2)
                while x in played_list:
                    x = randrange(2, 9, 2)
                    computerposition = x

            if danger_cnt3 == 0:
                corner = [1, 3, 7, 9]
                y = randrange(4)
                while corner[y] in played_list:
                    y = randrange(4)
                computerposition = corner[y]

            not_played_list.remove(computerposition)
            played_list.append(computerposition)
            position = computerposition

            play('X')
            print_board()
            a = winner_check('Player', 'Computer')
            if a == 0 or a == 1 or a == 2:
                break








