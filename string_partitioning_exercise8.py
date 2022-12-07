poem = """She could be a Norman Rockwell painting,
the small girl on my front porch with her eager
face, her wind-burned cheeks red as cherries.
Her father waits by the curb, ready to rescue
his child should danger threaten, his shadow
reaching halfway across the yard....
"""

poem_lines = (poem.lower()).splitlines()
print(poem_lines)

word = input('Give word: ')
word = (word.strip()).lower()
while not word.isalpha():
    word = input('All characters please: ')
    word = (word.strip()).lower()

for i in range(len(poem_lines)):
    if poem_lines[i].find(word) != -1:
        print(f'Line {i} : {poem_lines[i].replace(word, word.upper())}')





