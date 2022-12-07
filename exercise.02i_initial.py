string = 'I guess the only time most people think about injustice is when it happens to them'
my_list = list(string)
dictionary = {letter: 0 for letter in string}

for letter in string:
    dictionary[letter] += 1

for letter in sorted(dictionary.keys()):
    print(letter + ': ' + str(dictionary[letter]))
