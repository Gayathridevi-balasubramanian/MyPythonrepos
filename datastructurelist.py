''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

ITEM_AT_INDEX_THREE = student_pet_count_list[3]
# print(student_pet_count_list[100])
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]

NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)
SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)

# average = sum / number of items
AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)

print("--------------------------------------------------")
# multi dimensional lists

seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

# print(seating_chart[2][1])

for i, row in enumerate(seating_chart):
    print(f"students {row} in the row {i+1}")
    
print("--------------------------------------------------")

for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat {j+1}")
    
print("--------------------------------------------------")

# getting the index of the specific item ### LINEAR SEARCH IS USED


student_pet_count_list = [8,5,0,3,9,7]
ITEM =int( input("some data in interger : "))

def search(item, list):
    for data in student_pet_count_list:
        if data == ITEM:
            return True
    return False

        
print("value : ", search(ITEM, student_pet_count_list))
    

print("index at ", ITEM ," is : ",student_pet_count_list.index(ITEM))