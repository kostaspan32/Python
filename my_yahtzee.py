from random import randrange

#define player and computer scoring cards
player = {1: 0,
          2: 0,
          3: 0,
          4: 0,
          5: 0,
          6: 0,
          's': 0,
          'round_score' : 0
}

computer = {1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            's': 0,
            'round_score': 0
}

round_count = 0
player_rounds = 0
computer_rounds = 0

for round in range(6):

    round_count += 1

    #random turn choice
    player_move = randrange(0,2)
    turn = player
    if player_move == 0:
        turn = computer
        print('Computer plays first!')

    else:
        print('Player plays first!')

    #return counter to zero
    def zero_counter():
        player[1] = 0
        player[2] = 0
        player[3] = 0
        player[4] = 0
        player[5] = 0
        player[6] = 0
        player['round_score'] = 0
        computer[1] = 0
        computer[2] = 0
        computer[3] = 0
        computer[4] = 0
        computer[5] = 0
        computer[6] = 0
        computer['round_score'] = 0

    zero_counter()

    #choose best deuce
    def choose_best_deuce():

        # roll dice
        dice_list = []
        global my_list
        my_list = [0]

        for i in range(5):
            d = randrange(1, 7)
            dice_list.append(d)
        sum_list = []
        global next_range
        next_range = 5
        global max_dice_count
        max_dice_count = 0
        global max_dice
        max_dice = 0
        print(dice_list)
        for dice in dice_list:
            if dice_list.count(dice) > 1:
                sum_list.append(dice*dice_list.count(dice))
        if len(sum_list) > 0:
            global maximum
            maximum = max(sum_list)
        for dice in dice_list:
            if dice*dice_list.count(dice) == maximum:
                max_dice = dice
                max_dice_count = dice_list.count(dice)
        my_list[0] += max_dice_count
        print(f'Max dice is {max_dice} and count is {max_dice_count}')
        if sum_list == []:
            print('No pairs found!')

        if len(sum_list) > 0:
            turn[max_dice] += max_dice_count
            turn['s'] += max_dice * max_dice_count
            turn['round_score'] += dice_list.count(max_dice) * max_dice
            dice_list.pop(dice_list.index(max_dice)) * max_dice_count
            next_range -= max_dice_count



    choose_best_deuce()

    #repeat dice
    def repeat_dice():
        dice_list = []
        sum_list = []

        for i in range(5 - my_list[0]):
            d = randrange(1, 7)
            dice_list.append(d)
        print(dice_list)
        my_list[0] += dice_list.count(max_dice)

        if max_dice in dice_list:
            turn[max_dice] += dice_list.count(max_dice)
            turn['s'] += dice_list.count(max_dice) * max_dice
            print(f'{max_dice} found in list {dice_list.count(max_dice)} times')
            turn['round_score'] += dice_list.count(max_dice) * max_dice
            for j in range(dice_list.count(max_dice)):
                dice_list.pop(dice_list.index(max_dice))
            next_range = len(dice_list)
        else:
            print(f'Remaining deuce not paired with {max_dice}!')


    repeat_dice()
    repeat_dice()
    print(f'First score: {turn["round_score"]}')

    #change_turn
    if turn == player:
        turn = computer
        print('Computer turn!')
    else:
        turn = player
        print('Player turn!')
    choose_best_deuce()
    repeat_dice()
    repeat_dice()
    print(f'Second score: {turn["round_score"]}')

    print(f'Round results: Player score = {player["round_score"]} , computer score = {computer["round_score"]}')
    if player["round_score"] > computer["round_score"]:
        print(f'Player won round {round_count}!')
        player_rounds += 1

    elif computer["round_score"] > player["round_score"]:
        print(f'Computer won round {round_count}!')
        computer_rounds += 1

    else:
        print(f'Draw in round {round_count}!')

    zero_counter()


#pick_winner
print(f'Rounds are: Player rounds = {player_rounds} , Computer rounds = {computer_rounds}')
if player_rounds > computer_rounds:
    print('Player won!')

elif computer_rounds > player_rounds:
    print('Computer won!')

else:
    print('Draw!')