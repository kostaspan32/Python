day = input('What day is it today? : ')


if day == 'Saturday':
    print('I will study a bit')

elif day == 'Sunday':

    energy = input('How much energy do you have today? : ')

    if energy == 'None':
        print('I will rest today!')

    elif energy == 'A little':
        print('I will study a little today!')

    else:
        print('I will study a lot today!')

elif day == 'Monday':
    pass

