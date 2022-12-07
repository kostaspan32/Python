def favorite_author(name):
    if 'tolkien' in name.strip().lower():
        for i in range(500):
            print('Tolkien is the best')

    else:
        print(f'{name} is good!')

favorite_author('J.R. Tolkien')
favorite_author('J.K. Rowling')