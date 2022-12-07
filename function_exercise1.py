while True:

    def taste_check(favorite_movie):
        if 'batman' in favorite_movie:
            print('Good taste!')

        else:
            print('Awful taste!')


    taste_check(input('Please type your favorite movie! : ').strip().lower())