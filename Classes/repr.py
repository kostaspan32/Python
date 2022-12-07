class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'Time is : {str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:' \
               f'{str(self.seconds).zfill(2)}'

    def __repr__(self):
        return f'Time({self.hours},{self.minutes},{self.seconds})'


obj = Time(1, 1, 1)
print(obj)
print(repr(obj))

