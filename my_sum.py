cnt = 0
s = 0

while cnt <= 10:
    user_number = int(input('Please give ' + str(cnt) + 'th number: '))
    cnt += 1
    s += user_number

print(s)