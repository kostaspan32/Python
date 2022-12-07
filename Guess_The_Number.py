x = 45
cnt = 0
max_guesses = 5
print("Let's play a game! You have to guess the number I've hidden in " + str(max_guesses) + " attempts!")

guess = int(input('Make a guess! : '))

while guess != x:

    cnt += 1
    if cnt == max_guesses:
        print('Oops, you ran out of attempts! better luck next time!')
        break

    if guess < x:

        print('Nice try but... shoot for more!')

    if guess > x:

        print("Whoa there big fella... You 've overdone it!")

    guess = int(input('Make another guess! : '))

else:
    print('Congratulations, you found me!')
