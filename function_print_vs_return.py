def digit_find(number):
    cnt = 1

    while not str(number).strip().isdigit() or len(str(number).strip()) != 3:
        number = input('A three digit number please! : ')

    for digit in str(number):
        print(f'{cnt}st number: {digit} \n')
        cnt += 1


digit_find(32)

#alternatively find digit with:
#e.g. 352 % 10 == 2
#352//10 = 35
#35 % 10 = 5
#35//10 = 3

print('========================')
def digit_print(number):

    if not str(number).strip().isdigit() or len(str(number).strip()) != 3:
        return None

    third = number % 10
    number = number // 10
    second = number % 10
    first = number // 10
    return first, second, third


f, s, t = digit_print(352)

print(f)
print(s)
print(t)




digit_print(323)


