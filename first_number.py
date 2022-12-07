N = 15

if N == 0 or N == 1:
    print('It is not prime')

else:
    cnt = 0
    for i in range(2, N):
        if N % i == 0:
            cnt += 1
            if cnt == 1:
                print('It is not a first number')
                break
if cnt == 0:
    print(' It is a first number')



