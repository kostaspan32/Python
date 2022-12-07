my_list = ['a', 'b', 'c']
for letter in my_list:
    print(letter + ' ,', end='')

(print('\b\b'))
print(' ,'.join(my_list))