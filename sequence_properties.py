my_list = [1, 2, 3]
your_list = [4, 5, 6]
our_list = my_list + your_list

print(your_list * 4)
print(min(my_list))
print(max(your_list))
print(len(your_list))

print(our_list.count(2))

my_tuple = tuple(my_list)
my_list = list(my_tuple)

print(my_tuple)
print(my_list)

msg = 'Hello'
print(list(msg))

print(our_list.index(3, 1, 3))

print(list(range(4)))