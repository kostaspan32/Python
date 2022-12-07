my_dictionary = {
    'ιταμός': 'Προκλητικός, αυθάδης, αναιδής',
    'όνειδος': 'ντροπή, καταισχύνη',
    'πομφόλυγες': 'αερολογίες, ανοησίες'
}

print(my_dictionary)
my_dictionary['φληναφήματα'] = 'ανοησίες, σαχλαμάρες'
my_dictionary[input('Please type a key: ')] = input('Please type a value! : ')
print(my_dictionary)