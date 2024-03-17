def my_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(gen)

####################
def f(n):
    for i in range(1, n+1):
        yield i 
for i in f(2):
    print(i, end= ' ' )

lst = [x for x in range(5)]
print(lst)
lst = list(filter(lambda x : x%2 == 0 , lst))
print(lst)
print(len(lst))



