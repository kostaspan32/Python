l1 = [1, 2]
l2 = [2, 3]
l3 = l1 + l2
print(l1)
for elem in l1:
    l2.append(elem)

print(l2)
print(', '.join(str(_) for _ in l3))
