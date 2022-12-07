# draw lines (3 lists of 3 elements)
list0 = ['+--------+--------+--------+']
list1 = ['|', '', '|', '', '|', '', '|']
list2 = ['+--------+--------+--------+']
list3 = ['|', '', '|', '', '|', '', '|']
list4 = ['+--------+--------+--------+']
list5 = ['|', '', '|', '', '|', '', '|']
list6 = ['+--------+--------+--------+']

def print_list():

    print(list0)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    print(list6)


def player_move(player, mark):
    if player == 1:
        list1.pop(1)
        list1.insert(1, mark)

    if player == 2:
        list1.pop(3)
        list1.insert(3, mark)

    if player == 3:
        list1.pop(5)
        list1.insert(5, mark)

    if player == 4:
        list3.pop(1)
        list3.insert(1, mark)

    if player == 5:
        list3.pop(3)
        list3.insert(3, mark)

    if player == 6:
        list3.pop(5)
        list3.insert(5, mark)

    if player == 7:
        list5.pop(1)
        list5.insert(1, mark)

    if player == 8:
        list5.pop(3)
        list5.insert(3, mark)

    if player == 9:
        list5.pop(5)
        list5.insert(5, mark)


def player_move_check(player):
    if player == 'player1position':
        global player1position = int(input('Please type the position of your choice: '))
        while player1position in played_list:
            player1position = int(input('This position is not empty, pick another: '))

        while player1position > 9 or player1position < 1:
            player1position = int(input('Between 1 and 9 please: '))

    if player == 'player2position':
        global player2position = int(input('Please type the position of your choice: '))
        while player2position in played_list:
            player2position = int(input('This position is not empty, pick another: '))

        while player2position > 9 or player2position < 1:
            player2position = int(input('Between 1 and 9 please: '))


def winner_check(player, mark):

    print('Whoever plays first has O!')
    cnt = 0
    played_list = []

    for i in range(5):
        cnt += 1

        player_move_check('player1position')

        played_list.append(player1position)

        player_move(player1position, 'O')

        print_list()

        if list1[1] == list1[3] == list1[5] == mark:
            print(f'{player} won!')
            break

        if list3[1] == list3[3] == list3[5] == mark:
            print(f'{player} won!')
            break


        if list5[1] == list5[3] == list5[5] == mark:
            print(f'{player} won!')
            break

        if list1[1] == list3[1] == list5[1] == mark:
            print(f'{player} won!')
            break

        if list1[3] == list3[3] == list5[3] == mark:
            print(f'{player} won!')
            break

        if list1[5] == list3[5] == list5[5] == mark:
            print(f'{player} won!')
            break


        if list1[1] == list3[3] == list5[5] == mark:
            print(f'{player} won!')
            break

        if list5[1] == list3[3] == list1[5] == mark:
            print(f'{player} won!')
            break

        if cnt == 9:
            print('Draw')
            break

        cnt += 1
        player_move_check('player2position')

        while player2position == player1position:
            player2position = input('Different from player 1 please: ')

        player_move(player2position, 'X')

        print_list()


print_list()

winner_check('Player 1', 'O')
winner_check('Player 2', 'X')




#Repeat until cnt = 9 or until 3 x in a row or 3 o in a row
# Define in a row (kata 1? kata 3? kata 4?)
# Print 'Player x won' else print 'Draw'