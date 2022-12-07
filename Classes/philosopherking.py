from king import King
from philosopher import Philosopher

class PhilosopherKing(King, Philosopher):
    def __init__(self, kingdom, school):
        King.__init__(self, kingdom)
        Philosopher.__init__(self, school)


ma = PhilosopherKing('Rome', 'Stoics')
ma.think()
ma.rule()
ma.think()