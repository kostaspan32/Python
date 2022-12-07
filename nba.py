my_grades = [10, 10, 10, 3, 2, 6, 7]
passed = 0
sum_grades = 0

for grade in my_grades:
    if grade >= 5:
        passed += 1
        sum_grades += grade

print('My passed grades are ' + str(passed))
print('My average is ' + str(sum_grades/passed))
