cash_desk = []
cash_desk.insert(0, 'Tom')
cash_desk.append('Bob')
print(cash_desk)

first_client = cash_desk.pop(0)
print(first_client + ' has been served')

cash_desk.append('Pam')
cash_desk.append('Jim')
print(cash_desk)

second_client = cash_desk.pop(0)
print(second_client + ' has been served')
print(cash_desk)

third_client = cash_desk.insert(1, 'Stergiadis')
print(cash_desk)
print('Mr ' + cash_desk[1] + ' has stolen a place')