from queue import Queue
from random import randrange


class Bank:
    def __init__(self, N):
        self.queue_list = []
        self.N = N
        for _ in range(N):
            cnt = _ + 1
            obj = Queue(cnt)
            self.queue_list.append(obj)

    def customer_enters(self, full_name):
        x = randrange(self.N)
        self.queue_list[x].enqueue(full_name)
        print(f'{full_name} got in line {x + 1}')

    def customer_served(self):
        full_list = []
        for obj in self.queue_list:
            if len(obj) > 0:
                full_list.append(obj)
        if len(full_list) == 0:
            return 'No customers found!'
        y = randrange(len(full_list))
        print(f'{full_list[y].dequeue()} served in queue {full_list[y].number}!')

    def __str__(self):
        st = '\n' + '=' * 20
        for _ in self.queue_list:
            st += '\n' + str(_) + '\n'

        return f'Bank has: {st}'


b = Bank(3)
lt = [number*10 for number in range(1, 11)]
for i in range(100):
    if i in lt or i == 99:
        print('=' * 20)
        print(b)
        print('=' * 20)
    l = randrange(10)
    if l <= 6:
        b.customer_enters(f'Customer {i+1}')
    else:
        b.customer_served()
