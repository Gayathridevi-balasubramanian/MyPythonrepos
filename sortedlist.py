my_list = [1,7,3,4]
print(sorted(my_list))

print(sorted(my_list, reverse= True ))

student_grades = [('Sarah',89),('Rebacca',82),('Matt',91)]
print(sorted(student_grades))
#looks for the second entry of the order
print(sorted(student_grades, key=lambda x : x[1], reverse= True))

