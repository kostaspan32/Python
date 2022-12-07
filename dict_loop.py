hero_weapons = {
    'Beast': 'Claws',
    'Wolverine': 'Claws',
    'Spider-man': 'Web-Shoot',
    'Venom': 'Web-Shoot',
    'Hulk': 'Hands'
}

print ('Weapon gallery is: ', end='')
for weapon in set(hero_weapons.values()):
    print(weapon, end=', ')

print('\n', sorted(hero_weapons, reverse=True))

for key, value in sorted(hero_weapons.items()):
    print(key + ' has ' + value)

for key in sorted(hero_weapons.keys()):
    print(key + ' has ' + hero_weapons[key])
