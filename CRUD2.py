from lesson import Lesson
student_list = []
algebra = Lesson('algebra')
geometry = Lesson('geometry')
history = Lesson('history')
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
                               'Lessons': input('Enrolled in lessons (algebra, geometry, history) : '),
                               'ID': str(ID)
                               }
    student_dictionary.update(student_dictionary_rest)
    if 'algebra' in student_dictionary_rest['Lessons']:
        algebra.lesson_pupil_list.append(student_dictionary_rest['ID'])
    if 'geometry' in student_dictionary_rest['Lessons']:
        geometry.lesson_pupil_list.append(student_dictionary_rest['ID'])
    if 'history' in student_dictionary_rest['Lessons']:
        history.lesson_pupil_list.append(student_dictionary_rest['ID'])
    with open('lessons.json', 'a') as f:
        f.write()

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

def main():

    while True:

        cnt = 0
        for student in student_list:
            cnt += 1
            print('=' * 20)
            print(f'Student {cnt}')
            for key in student.keys():
                print(f'{key} is: {student[key]}')
        print('=' * 20)
        print('Menu: \n1. New Registration \n2. Print \n3.Update Registration \n4.Delete Registration\n5.Exit')
        user_input = input('Make a choice: ')

        if user_input == '1':
            create_pupil()

        if user_input == '2':
            if student_list == []:
                print('No pupils in student list!')
                continue
            pupil_ID = 0
            pupil_name = ''
            pupil_surname = ''
            choice = int(input('Please type pupil ID (0) or student name and surname(1): (choose 0 or 1) :  '))
            while choice not in [0, 1]:
                choice = int(input('Please type pupil ID (0) or student name and surname(1): (choose 0 or 1) :  '))

            if choice == 0:
                pupil_ID = int(input('ID : ').strip())
                print_pupil(pupil_ID, pupil_name, pupil_surname)
            elif choice == 1:
                pupil_name = input('Name: ').strip()
                pupil_surname = input('Surname: ').strip()
                print_pupil(pupil_ID, pupil_name, pupil_surname)

        if user_input == '3':
            search_item = input('Would you like to search by ID or by surname? : ').strip().lower()
            if search_item == 'id':
                found = 0
                search_item = input('Please insert ID: ').strip()
                for student in student_list:
                    if student['ID'] == search_item:
                        found += 1
                        print(student)
                        update_choice = input('Which attribute would you like to update? : ')

                        while update_choice not in student:
                            update_choice = input('Please type a student attribute correctly! : ')

                        if update_choice in student:
                            student[update_choice] = input(f'Please insert new {update_choice}: ')
                            print(f'New registration: {student}')
                            continue

                    if found == 0:
                        print('Wrong ID!')
                        continue

            if search_item == 'surname':
                update_surname = input('Please type student surname: ')
                surname_list = search_pupil_by_surname(update_surname)
                if len(surname_list) > 1:
                    found = 0
                    print(surname_list)
                    update_id = input('Please pick a student ID: ')
                    for student in student_list:
                        if student['ID'] == update_id:
                            found += 1
                            print(student)
                            update_choice = input('Which attribute would you like to update? : ')

                            while update_choice not in student:
                                update_choice = input('Please type a student attribute correctly! : ')

                            if update_choice in student:
                                student[update_choice] = input(f'Please insert new {update_choice}')
                                print(f'New registration: {student}')
                                continue

                        if found == 0:
                            print('Wrong ID!')
                            continue

        if user_input == '4':
            search_item = input('Would you like to search by ID or by surname? : ').strip().lower()
            while search_item not in ['id', 'surname']:
                search_item = input('ID or surname? : ').strip().lower()
            if search_item == 'id':
                found = 0
                search_item = input('Please insert ID: ').strip()
                for student in student_list:
                    if student['ID'] == search_item:
                        found += 1
                        print(student)
                        user_choice = input('Would you like to delete student?').strip().lower()
                        while user_choice not in ['yes', 'no']:
                            user_choice = input('Type yes or no please! : ').strip().lower()
                        if user_choice == 'yes':
                            delete_pupil_by_id(student['ID'])

                    if found == 0:
                        print('Wrong ID!')
                        continue

            if search_item == 'surname':
                delete_surname = input('Please type student surname: ')
                surname_list = search_pupil_by_surname(delete_surname)
                if len(surname_list) > 1:
                    found = 0
                    print(surname_list)
                    delete_id = input('Please pick a student ID: ')
                    for student in student_list:
                        if student['ID'] == delete_id:
                            found += 1
                            print(student)
                            user_choice = input('Would you like to delete student? : ').strip().lower()
                            while user_choice not in ['yes', 'no']:
                                user_choice = input('Type yes or no please! : ').strip().lower()
                            if user_choice == 'yes':
                                delete_pupil_by_id(student['ID'])

                            if found == 0:
                                print('Wrong ID!')
                                continue
        if user_input == '5':
            break


main()