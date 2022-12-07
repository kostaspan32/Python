# def c(n, k):
#     while k <= 0:
#         k = input('Please put positive number: ')
#
#     cnt = 0
#     if n == k:
#         return 1
#
#     elif k == 1:
#         return n
#
#     for i in range(k):
#         cnt += c(n - k + 1, 1) + c(n - k + 1, 2)
#
#     return cnt
#
#
# print(c(4, 2))

def C(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    else:
        return C(n-1, k-1) + C(n-1, k)


print(C(3, 2))
