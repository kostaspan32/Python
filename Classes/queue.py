class Queue:
    def __init__(self, number=0):
        self.number = number
        self.array = []

    def enqueue(self, item):
        self.array.append(item)

    def dequeue(self):
        if not self.array:
            return None
        else:
            return self.array.pop(0)

    def __repr__(self):
        return f'Queue({self.number},{self.array})'

    def __str__(self):
        return f'Queue {self.number} is : {",".join(self.array)}'

    def __add__(self, other):
        if isinstance(other, Queue):
            new_array = self.array + other.array
            return Queue(self.number, new_array)
        elif isinstance(other, list):
            new_array = self.array + other
            return Queue(self.number, new_array)
        elif isinstance(other, str):
            new_q = Queue()
            new_q.array = self.array.copy()
            new_q.enqueue(other)
        return new_q

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.array += other.array
        elif isinstance(other, list):
            self.array += other
        elif isinstance(other, str):
            self.enqueue(other)
        return self

    def __neg__(self):
        return self.dequeue()

    def __len__(self):
        return len(self.array)


obj1 = Queue(1)
obj2 = Queue(2)
obj1.enqueue('Tasos')
obj2.enqueue('Ritas')





