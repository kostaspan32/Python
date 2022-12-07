even_set = set()
three_set = set()
odd_set = set()
primes_list = []


for number in range(0, 100+1):
    if number % 2 == 0:
        even_set.add(number)

print(even_set)

for number in range(0, 100+1):
    if number % 2 == 1:
        odd_set.add(number)

print(odd_set)

for number in range(0, 100+1):
    if number % 3 == 0:
        three_set.add(number)

print (three_set)


for number in range(2, 100+1):
    for i in range(2, number):
        if number % i == 0:
            break

    else:
        primes_list.append(number)


undivided_set = set(primes_list)

print(even_set & three_set)
print(odd_set & undivided_set)
print(undivided_set - odd_set)
print(undivided_set ^ odd_set)

