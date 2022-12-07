memory_list = [1, 3, 4, 4, 2, 1, 2, 3]
player_list = []

for i in range(8):
    player_list.append('y')

print(player_list)
print('Pick two cards from this list. If they are the same, they will be removed! Tou win when the cards are finished')

for i in range(4):

    picked_card1 = int(input('Please pick the first card! : '))
    print('The ' + str(picked_card1) + 'th card is ' + str(memory_list[picked_card1]))
    picked_card2 = int(input('Please pick the second card! : '))

    while picked_card1 == picked_card2:
        print('Please pick different cards!')
        picked_card1 = int(input('Please pick the first card! : '))
        picked_card2 = int(input('Please pick the second card! : '))

    while memory_list[picked_card1] != memory_list[picked_card2]:
        print('The cards are not the same, try again!')
        picked_card1 = int(input('Please pick the first card! : '))
        picked_card2 = int(input('Please pick the second card! : '))

    if memory_list[picked_card1] == memory_list[picked_card2]:

        if i == 3:
            print('Congratulations, you won!')
            break
        x = memory_list[picked_card1]
        memory_list.remove(x)
        memory_list.remove(x)
        player_list.remove('y')
        player_list.remove('y')
        player_list.insert(picked_card1, x)
        player_list.insert(picked_card2, x)
        print('You succeeded, ' + str(3-i) + ' more pairs left!')
        print(player_list)

