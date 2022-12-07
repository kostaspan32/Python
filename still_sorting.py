N = int(input('Please type a number between 3 and 20: '))
my_list = []

while N < 3 or N > 20:
    N = int(input(('Please type a correct number! : ')))

for cnt in range(0,N):
    my_list.append(int(input('Give ' + str(cnt+1) + 'th number: ')))


my_list.sort()
print(my_list)


