student_list = []

def create_pupil():
    if student_list == []:
        ID = 1000
    else:
        ID = int(student_list[len(student_list) - 1]['ID']) + 1
        print(f'Current pupil ID: {ID}')
    kofths = 0
    student_dictionary = {'Name': input('Please type student name: '),
                          'Surname': input('Please type student surname: '),
                          'Father name': input('Please type father name: ')}

    for student in student_list:
        if student_dictionary['Name'] == student['Name'] and student_dictionary['Surname'] == student['Surname'] and \
                student_dictionary['Father name'] == student['Father name']:
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
            return

    student_dictionary_rest = {'Age': input('Please type age: '),
                               'Class': input('Please type class: '),
                               'Identity Number': input('Please type identity number: '),
                               'ID': str(ID)
                               }
    student_dictionary.update(student_dictionary_rest)

    ID += 1
    print(f'Next available ID: {ID}')
    student_list.append(student_dictionary)
    print('Registration confirmed!')
    print(student_dictionary)
    student_dictionary = {}


def print_pupil(pupil_ID, pupil_name, pupil_surname):
    finder = 0

    for student in student_list:
        if pupil_ID == int(student['ID']) or pupil_name + pupil_surname == student['Name'] + student['Surname']:
            print(student)
            finder += 1

    if finder == 0:
        print('Pupil not found!')

def search_pupil_by_surname(surname):
    match_students = []
    for student in student_list:
        if surname == student['Surname']:
            match_students.append(student)

    return match_students

def delete_pupil_by_id(pupil_id):
    found = 0
    for student in student_list:
        if student['ID'] == pupil_id:
            found += 1
            student_list.remove(student)
            print('Deletion complete!')
    if found == 0:
        print('Wrong ID!')