grades = list()

def filter_grade(grade):
    return grade != 'F'

while True:
    print(f'add your grades and we\'ll get you new \'F\' free grades.')
    add_grade = input('What grade would you like to add to the list? (eg. A, B, F, etc) ')
    add_another = input('Would you like to add another grade? (y/n) ')

    if add_another == 'n':
        grades.append(add_grade)
        break
    else:
        grades.append(add_grade)
        continue

# updated_grades = list()
#
# for grade in grades:
#     if filter_grade(grade) == True:
#         updated_grades.append(grade)
#
# print(updated_grades)

# print([grade for grade in grades if filter_grade(grade) == True])

print(list(filter(filter_grade, grades)))
