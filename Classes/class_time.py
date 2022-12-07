class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_hours(self):
        x = int(input('Please type hours (0-23) : '))
        while x not in range(24):
            x = x = int(input('0-23 please! : '))
        self.hours = x

    def set_minutes(self):
        y = int(input('Please type minutes (0-59) : '))
        while y not in range(60):
            y = int(input('0-59 please! : '))
        self.minutes = y

    def set_seconds(self):
        z = int(input('Please type seconds (0-59) : '))
        while z not in range(60):
            y = int(input('0-59 please! : '))
        self.seconds = z

    def set_time(self):
        self.set_hours()
        self.set_minutes()
        self.set_seconds()

    def total_seconds(self):
        s = self.hours*3600 + self.minutes*60 + self.seconds
        return s

    def __str__(self):
        return f'Time is : {str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}'

    def next_seconds(self):
        seconds = (self.seconds + 1) % 60
        carry = seconds // 60
        minutes = (self.minutes + carry) % 60
        carry = minutes//60
        hours = (self.hours + carry) % 24
        next_object = Time(hours, minutes, seconds)
        return next_object

    def __add__(self, other): #pio kompso an new_seconds, new_minutes, new_hours
        if isinstance(other, Time):
            carry1 = (self.seconds + other.seconds) // 60
            new_seconds = (self.seconds + other.seconds) % 60
            carry = (self.minutes + other.minutes + carry1) // 60
            new_minutes = (self.minutes + other.minutes + carry1) % 60
            new_hours = (self.hours + other.hours + carry) % 24
            return Time(new_hours, new_minutes, new_seconds)

        elif isinstance(other, int):
            new_hours = (self.hours + other) % 24
            return Time(new_hours, self.minutes, self.seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return f'Time({str(self.hours).zfill(2)},{str(self.minutes).zfill(2)},{str(self.seconds).zfill(2)})'


now = Time(16, 6, 20)
print(now)
now.set_time()
print(now)
print(now.next_seconds())
print(now + now.next_seconds())
print(now + 4)
print(4 + now)

