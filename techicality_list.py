english = 28
russian = 55
french = 20

party_list = [russian, english, french]

party_list.append(4)
party_list.insert(1, 1)
party_list.extend([1, 2, 3])
print(party_list)

last = party_list.pop()
print(party_list)
print(last)

party_list.pop(4)
print(party_list)

party_list.remove(1)
party_list.remove(1)
print(party_list)




