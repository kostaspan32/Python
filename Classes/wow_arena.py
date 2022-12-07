from wow_character import Character
from random import randrange

class Arena:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    def print_state(self):
        print('Team A')
        for character in self.team_a:
            print(character)
        print('=' * 20)

        print('Team B')
        for character in self.team_b:
            print(character)
        print('=' * 20)

    def play(self):
        time = -1
        while True:
            time += 1
            print('=' * 20)
            print('Time = ' + str(time))
            print('='*20)
            self.print_state()
            playable_characters = []
            for character in self.team_a:
                if character.delay == 0:
                    playable_characters.append(('A', character))

            for character in self.team_b:
                if character.delay == 0:
                    playable_characters.append(('B', character))

            for character in playable_characters:
                attacking = character[1]
                if character[0] == 'A':
                    defending = self.team_b[randrange(len(self.team_b))]

                else:
                    defending = self.team_a[randrange(len(self.team_a))]

                damage = attacking.attack()
                defending.health -= damage
                print(f'{attacking.name} dealt {damage} to {defending.name}')

            for pos in range(len(self.team_a)-1, -1, -1):
                if self.team_a[pos].is_dead():
                    print(f'{self.team_a[pos].name} is dead!')
                    self.team_a.pop(pos)

            for pos in range(len(self.team_b)-1, -1, -1):
                if self.team_b[pos].is_dead():
                    print(f'{self.team_b[pos].name} is dead!')
                    self.team_b.pop(pos)

            if len(self.team_a) == 0:
                print('Team B won!')
                break

            elif len(self.team_b) == 0:
                print('Team A won!')
                break

            for character in self.team_a:
                character.end_round()

            for character in self.team_b:
                character.end_round()

            input('Press enter to continue! : ')


