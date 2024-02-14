class Book:
    def __init__(self, name):
        self.name = name
    
class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("The Wing Of Fire!")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Wastington Port")
n2 = Newspaper("The New York Times")

print(type(b1))
print(type(b2))
print(type(n1))
print(type(n2))

print("Tells whether it is an instance or not!")
print(isinstance(b1, (Book, Newspaper)))
print(isinstance(n2, Newspaper))

