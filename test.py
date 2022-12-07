def player_move_check(player):
    global player = int(input('Please type the position of your choice: '))
    while player in played_list:
        player = int(input('This position is not empty, pick another: '))

    while player > 9 or player < 1:
        player = int(input('Between 1 and 9 please: '))


player_move_check(player1position)
print(player1position)