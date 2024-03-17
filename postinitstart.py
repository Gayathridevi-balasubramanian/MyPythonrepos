from dataclasses import dataclass, field
import random

# @dataclass
# class Book:
#     # adding default values
#     title : str  = "No Tiltle"
#     author : str = "No Author"
#     pages : int  = 0 
#     price : float 

#     def __post_init__(self):
#         self.description = f"{self.title} by {self.author} by {self.pages}"
# # non default arguement should follow the default arguements
# b1 = Book("War and Peace","Leo Tolstoy",1225,39.95)
# b2 = Book("The Catcher in the Rye","JD Salinger",234,29.95)

# print(b1.description)
# print(b2.description)



@dataclass
class Book:
    # adding default values
    title : str  = "No Tiltle"
    author : str = "No Author"
    pages : int  = 0  
    price : float = field(default = 10.0)

    def __post_init__(self):
        self.description = f"{self.title} by {self.author} by {self.pages}"
# non default arguement should follow the default arguements
b1 = Book("War and Peace","Leo Tolstoy",1225)
b2 = Book("The Catcher in the Rye","JD Salinger",234,45.54)

print(b1.description)
print(b2.description)


# random generation of the data

def price_func():
    return float(random.randrange(20,40))
@dataclass
class Book:
    # adding default values
    title : str  = "No Tiltle"
    author : str = "No Author"
    pages : int  = 0  
    price : float = field(default_factory = price_func)

    

    def __post_init__(self):
        self.description = f"{self.title} by {self.author} by {self.pages}"
# non default arguement should follow the default arguements
b1 = Book("War and Peace","Leo Tolstoy",1225)
b2 = Book("The Catcher in the Rye","JD Salinger",234)

print(b1.description)
print(b2.description)




#################################
# to set one of the attribute to none 
# and assign value after initialization
#########################################

@dataclass
class Person:
    name: str = "John Doe"
    age: int = 35
    city: str = "New York"
    occupation: str = field(default=None)

# Creating an instance with default values
person1 = Person()
print(person1)  # Output: Person(name='John Doe', age=35, city='New York', occupation=None)

# Creating an instance with custom values
person2 = Person(name="Alice", age=28, city="San Francisco", occupation="Software Engineer")
print(person2)  # Output: Person(name='Alice', age=28, city='San Francisco', occupation='Software Engineer')

# Assigning a value to 'occupation' after initialization
person2.occupation = "Data Scientist"
print(person2)  