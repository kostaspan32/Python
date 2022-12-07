best_friends = ['Dospras', 'Soulounias', 'Spuros']
invited = ['Hlektra', 'Dwra', 'Angelopoulos', 'Tzina', 'Xrisanthi', 'Stauros', 'Christian', 'Xrhstos', 'Nwntas', 'Xatzhanastashs']
cnt = 0

for friend in best_friends:

    if friend in invited:
        cnt += 1
        if cnt == 2:
            print('I will go to the party!')
            break

if cnt < 2:
    print('I will not go to the party!')



