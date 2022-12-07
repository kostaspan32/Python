class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'Time is : {str(self.hours).zfill(2)} / {str(self.minutes).zfill(2)} / {str(self.seconds).zfill(2)}'


t = Time(9, 26, 5)
print(t) #tupwnei to str tou
print(str(t))
