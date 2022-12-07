is_geek = input('Do you think you are a geek? : ')

computer_hours = int(input('How many hours do you spend on the computer per day? : '))

training_hours = int(input('How many hours do you exercise per day? : '))

virgin_test = input('Are you a virgin? : ')


if (is_geek == 'Yes' and (computer_hours >= 4 or training_hours < 0.5) and (virgin_test != 'No') or (is_geek == 'No' and (computer_hours < 4 or training_hours >= 0.5) and (virgin_test == 'No'))):
    print('You are telling the truth')

else:
    print('You are a liar')