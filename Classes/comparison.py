class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds > other.seconds:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Time):
            if self.hours > other.hours:
                return True
            elif self.hours == other.hours:
                if self.minutes > other.minutes:
                    return True
                elif self.minutes == other.minutes:
                    if self.seconds >= other.seconds:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif isinstance(other, int):
            obj = Time(other, 0, 0)
            return self > obj

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True




t = Time(9, 49, 4)
t2 = Time(9, 49, 4)
print(t.__gt__(t2))
print(f't > t2: {t > t2}')
print(f't >= t2: {t >= t2}')
print(f't = t2: {t == t2}')
print(f't != t2: {t != t2}')
print(f't < t2: {t < t2}')
print(f't <= t2: {t <= t2}')
print(f't >= 10: {t >= 10}')


