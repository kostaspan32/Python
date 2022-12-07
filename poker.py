from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 52
deck = []
jack = 11
queen = 12
king = 13
ace = 14

#create numbers list
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace]
#create shape list
shapes = ['hearts', 'spades', 'diamond', 'club']
#create tuple for each card
for number in numbers:
    for shape in shapes:
        card_tuple = [number, shape]
        deck.append(card_tuple)

print('Deck is ' + str(deck))

player1 = []
player2 = []

for i in range(5):

    position = randrange(len(deck))
    drawn_card = deck.pop(position)
    player1.append(drawn_card)

    position = randrange(len(deck))
    drawn_card = deck.pop(position)
    player2.append(drawn_card)

print('Player 1 has: ' + str(player1))
print('Player 2 has: ' + str(player2))

cnt1 = 0
for card in player1:
    if ace in card:
        cnt1 += 1
        if cnt1 == 4:
            print('Player 1 has four of a kind on ace')

cnt2 = 0
for card in player2:
    if ace in card:
        cnt2 += 1
        if cnt2 == 4:
            print('Player 2 has four of a kind on ace')


straight_check = []

for card in player1:
    straight_check.append(card[0])

straight_check.sort()

sum_differences = 0
for i in range(1, 5):
    difference = straight_check[i] - straight_check[i-1]
    if difference == 1:
        sum_differences += 1

if sum_differences == 4:
    print('Player 1 has straight')




straight_check2 = []

for card in player2:
    straight_check2.append(card[0])

straight_check2.sort()

sum_differences = 0
for i in range(1, 5):
    difference = straight_check2[i] - straight_check2[i-1]
    if difference == 1:
        sum_differences += 1

if sum_differences == 4:
    print('Player 2 has straight')












