cnt = 0
primes_list = []

for N in range(2, 100+1):
    for i in range(2, N):
        if N % i == 0:
            break

    else: primes_list.append(n)



primes_tuple = tuple(my_list)
print(primes_tuple)