primary_colors = set(["RED","BLUE","GREEN"])

Color = "GREEN"

if Color in primary_colors:
    print("It is a primary colors")
else:
    print(" It is not a primary colors")


letters = set(['a', 'b'])
letters.add('c')
print(letters)

# working on sets
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

union_set = set1.union(set2)
print(union_set)

inter_set = set1.intersection(set2)
print(inter_set)

diff_set = set1.difference(set2)
print(diff_set)

diff_set = set2.difference(set1)
print(diff_set)

symdiff_set = set1.symmetric_difference(set2)
print(symdiff_set)

# making the set immutable
primary_colors = frozenset(["RED","GREEN","BLUE"])
primary_colors.add("green")