from random import randint
from collections import Counter

def roll_dice( *dice, no_of_trails= 1_000_000):
    # create a counter to store the count of the each outcome
    counts = Counter()
    # simulate the rolling of dice for the specific number of 
    for _ in range(no_of_trails):
        counts[sum(randint(1, sides) for sides in dice)] += 1
    
    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice)+1):
        print(f'\n{outcome}\t{counts[outcome] * 100 / no_of_trails : 0.2f}%')

roll_dice(6)
roll_dice(6,6)
roll_dice(6,6,6,no_of_trails=500)

print("the sample of what the counter is")
my_list = [1, 2, 3, 1, 2, 3, 4, 5]
print(f'{my_list}')
my_counter = Counter(my_list)
print("the counter is",my_counter)
print(my_counter[2])  # Output: 2 (since 2 appears twice in my_list)
another_list = [1, 2, 3, 4, 5, 1, 2, 3]
my_counter.update(another_list)
print(my_counter)
print("the elements() returns the counter into reality numbers\n",list(my_counter.elements()))
# Output: [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]
print("the mostcommon() function returns the n th most common elements and it occurence in the counter\n",my_counter.most_common(2))
# Output: [(2, 4), (3, 4)]

counter1 = Counter(a=3, b=1)
counter2 = Counter(a=1, b=2)

# Addition
result = counter1 + counter2
print("Addition",result)
# Output: Counter({'a': 4, 'b': 3})

# Subtraction
result = counter1 - counter2
print("Subtraction",result)
# Output: Counter({'a': 2})


