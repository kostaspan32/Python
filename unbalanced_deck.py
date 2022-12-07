from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

def player1_pick():
    player1.add(deck.pop())

#oxi px player1.add(deck.pop(randrange(len(deck))) epeidh deck = sunolo ara tuxaia seira
#afou apousia diatakshs den exei nohma deck(x)

def player2_pick():
    player1.add(deck.pop())


def play():
    print('Let the game begin!')
    for _ in range(len(deck)):

        if randrange(2) == 0:
            player1_pick()

        else:
            player2_pick()

    print(f'Player 1: {len(player1)} cards')
    print(f'Player 2: {len(player2)} cards')

    if len(player1) > len(player2):
        print('Player 1 won!')

    if len(player2) > len(player1):
        print('Player 2 won!')

    if len(player1) == len(player2):
        print('Draw!')



kind = {'heart', 'diamond', 'spade', 'club'}
number = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}

deck = {(k , n) for k in kind for n in number}

player1 = set()
player2 = set()

play()