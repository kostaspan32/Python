from wow_character import Character
from wow_arena import Arena
from random import randrange

def main():
    orcs = [Character('orc-' + str(i+1), 2, randrange(4)) for i in range(5)]
    nightelves = [Character('Night Elf-' + str(i + 1), 3, randrange(3)) for i in range(5)]

    a = Arena(orcs, nightelves)
    a.play()

main()