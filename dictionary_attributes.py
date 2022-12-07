working_man = {
    'Όνομα': input('Please type your name: '),
    'Επώνυμο': input('Please type your surname: '),
    'Πατρώνυμο': input("Please type your father's name: "),
    'Ημερομηνία γέννησης': input('Please type date of birth: '),
    'Διεύθυνση': input('Please type address: '),
    'Τηλέφωνο': input('Please type phone number: ')
}

full_name = working_man['Όνομα'] + '' + working_man['Επώνυμο']
print('Ονοματεπώνυμο: ' + full_name)
print('Ημ/νία Γέννησης: ' + working_man['Ημερομηνία γέννησης'])
print('Διεύθυνση: ' + working_man['Διεύθυνση'])
print('Τηλέφωνο: ' + working_man['Τηλέφωνο'])

if 'ΑΜΚΑ' not in working_man:
    print(working_man['Όνομα'] + ' has no AMKA!')