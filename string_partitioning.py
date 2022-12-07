quote = 'I don\'t hate them... I just feel better when they are not around'
print(quote)

word = input('Give word : ')
word = (word.strip()).lower()

quote_lowered = quote.lower()

while True:
    if word.isalpha():
        if word in quote_lowered:
            print(quote.replace(word, word.upper()))
            break
        else:
            word = input('Word not in quote, please type another word! : ')
            word = (word.strip()).lower()

    else:
        word = input('Only characters please:')
        word = (word.strip()).lower()


