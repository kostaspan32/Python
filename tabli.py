zari_1 = int(input('Player 1, how much came the first zari? : '))
zari_2 = int(input('Player 1, how much came the second zari? : '))

athroisma_1 = zari_1 + zari_2

zari_3 = int(input('Player 2, how much came your first zari? : '))
zari_4 = int(input('Player 2, how much came your secoond zari? : '))

athroisma_2 = zari_3 + zari_4

if athroisma_1 > athroisma_2:
    print('Player 1 should play first!')

elif athroisma_1 < athroisma_2:
    print('Player 2 should play first!')

else:
    print('Throw the dice again!')