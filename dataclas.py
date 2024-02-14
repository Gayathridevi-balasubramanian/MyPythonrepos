from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
# can also define the normal classes
    def bookinginfo(self):
        return f"{self.title} by {self.author}"
    
    def __post_init__(self):
        self.description  = f"{self.title} by {self.author} , {self.pages} pages"



# create some instances    
B1 = Book("War and peace","Loe Tolstoy", 968, 23.56)
B2 = Book("The catcher in the rail ","JD Sailgerr", 234,56.76 )
B3 = Book("War and peace","Loe Tolstoy", 968, 23.56)

#access field 
print(B1.title)
print(B2.author)

# __repr__ method 
print(B1)

# __eq__ methos
print(B1 == B3)
print(B1 == B2)

# accessing the methods
print(B1.bookinginfo())
B1.title = "Anna Karinea"
print("changed to:", B1.bookinginfo())

# accessing the postinit class
# note that the title name is unchanged after the changes
print(B1.description)
print(B2.description)