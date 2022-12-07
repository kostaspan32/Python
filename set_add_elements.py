my_set = {1, 2, 3}
my_set2 = my_set.copy()
my_set.update((3, 5))
print(my_set)
my_set.remove(3)
print(my_set)
my_set.discard(5)
print(my_set)
print(my_set2)