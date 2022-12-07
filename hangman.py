word = 'Morning'

gameword = word.lower()
gameword_list = list(gameword)
gameword_list2 = gameword_list.copy()
hidden_letters = []
guessed_letters_in_gameword = []
cnt = 0
cnt_list = []
letters_remaining = len(gameword_list)

for letter in gameword:
    hidden_letters.append('_')

print(f'Word is {hidden_letters}')


attempts_count = 10

guest_input = input(f'Please guess a letter! You have {attempts_count} attempts: ').strip().lower()

while guest_input.isalpha() == False or len(guest_input) > 1:
    guest_input = input(f'Only one letter! You have {attempts_count} attempts: ').strip().lower()

attempts_count -= 1

while True:

    while guest_input in hidden_letters:
        guest_input = input(f'The letter you typed is already guessed! You have {attempts_count} attempts: ').strip().lower()
        print(hidden_letters)

        while guest_input.isalpha() == False or len(guest_input) > 1:
            guest_input = input(f'Only one letter! You have {attempts_count} attempts: ').strip().lower()

    if guest_input not in gameword_list:
        if attempts_count == 0:
            print(f'You lost! Word was {gameword}')
            break

        guest_input = input(f'The letter you typed is not in word! You have {attempts_count} attempts: ').strip().lower()
        print(hidden_letters)

        while guest_input.isalpha() == False or len(guest_input) > 1:
            guest_input = input(f'Only one letter! You have {attempts_count} attempts: ').strip().lower()

        while guest_input in hidden_letters:
            guest_input = input(f'The letter you typed is already guessed! You have {attempts_count} attempts: ').strip().lower()
            print(hidden_letters)

            while guest_input.isalpha() == False or len(guest_input) > 1:
                guest_input = input(f'Only one letter! You have {attempts_count} attempts: ').strip().lower()

        attempts_count -= 1

    if guest_input in gameword_list:

        for letter in gameword_list:
            if letter == guest_input:
                cnt_list.append(cnt)

            cnt += 1

        for cnt in cnt_list:
            letters_remaining -= 1
            hidden_letters[cnt] = guest_input

        print(f'Correct! Word is {hidden_letters} ')

        if letters_remaining == 0:
            print('You won!!')
            break

        guest_input = input(f'Please guess a letter! You have {attempts_count} attempts: ').strip().lower()

        while guest_input.isalpha() == False or len(guest_input) > 1:
            guest_input = input(f'Only one letter! You have {attempts_count} attempts: ').strip().lower()

        attempts_count -= 1
        cnt = 0
        cnt_list = []







