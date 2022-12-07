my_list = ['Pulp Fiction', 'Game', 'Avatar', 'Titanic' ]

request = input('Please type your next favorite movie: ')

if request in my_list:
    print('Name already on list, no save')

if request not in my_list:
    my_list.append(request)
    my_list.sort()
    print(my_list)
    print(len(my_list))
