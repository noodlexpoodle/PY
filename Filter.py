gpa = []
i = 1
while i == 1:
    var = input('Enter your grade. Type "Done" to finish ')
    if var.lower() == 'done':
        i = 0
    else:
        gpa.append(var)
print(gpa)

#by filter
def remove_bad_grade (grade):
    return grade !='F'
print(list(filter(remove_bad_grade,gpa)))

#by loop
no_fail = []
for grade in gpa:
    if grade != 'F':
        no_fail.append(grade)
print(no_fail)

#by comprehension
no_fail = [grade for grade in gpa if grade != 'F']
print(no_fail)

#by map
def remove_bad_grade_v2(grade):


no_fail = list(map(remove_bad_grade,gpa))
print(no_fail)
