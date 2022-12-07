ID = 1000
student_list = []
kofths = 0

while True:

    print('Menu: \n1. New Registration \n2. Print \n3.Update Registration \n4.Delete Registration\n5,Exit')
    print(f"list is {student_list}")
    user_input = input('Make a choice: ')

    if user_input == '1':
        student_dictionary = {'Name': input('Please type student name: '),
                              'Surname': input('Please type student surname: '),
                              'Father name': input('Please type father name: ')}

        for student in student_list:
            if student_dictionary['Name'] == student['Name'] and student_dictionary['Surname'] == student['Surname'] and student_dictionary['Father name'] == student['Father name']:
                user_choice = input('Student already listed! Do you wish to make new entry? : ').strip().lower()
                while user_choice != 'yes' and user_choice != 'no':
                    user_choice = input('I do not understand. Yes or no?')

                if user_choice == 'no':
                    kofths += 1
                    break

                if user_choice == 'yes':
                    print('Proceed entering the rest details!')

        if kofths == 1:
            print('Entry cancelled. Return to menu!')
            kofths = 0
            continue

        student_dictionary_rest = {'Age': input('Please type age: '),
                                   'Class': input('Please type class: '),
                                   'Identity Number': input('Please type identity number: '),
                                   'ID': str(ID)
                                   }
        student_dictionary.update(student_dictionary_rest)

        ID += 1
        student_list.append(student_dictionary)
        print('Registration confirmed!')
        print(student_dictionary)

        student_dictionary = {}
