age = int(input('What is your age? : '))

if age < 18:
    print('You are underage!')

elif 18 <= age < 65:
    print('You are an adult')

else:
    print('You are retired!')