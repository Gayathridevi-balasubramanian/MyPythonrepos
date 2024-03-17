#
#

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by author {self.author} , costs {self.price}"
    
    def __repr__(self):
        return f"title = {self.title}, author = {self.author} , costs= { self.price}"
    
    #equality operator
    def __eq__(self,value):
        if not isinstance(value, Book):
            raise ValueError("the object instance doesn't belong to the book")
        return(self.title == value.title and self.author == value.author and self.price == value.price)
    # less than operator
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("the object instance doesn't belong to the book")
        return (self.price < value.price)
    
    # greater than equal to 
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("the object instance doesn't belong to the book")
        return (self.price >= value.price)

B1 = Book("War and peace","Loe Tolstoy", 23.56)
B2 = Book("The catcher in the rail ","JD Sailgerr", 56.76 )
B3 = Book("War and peace","Loe Tolstoy", 23.56)
B4 = Book("To Kill A Mocking Bird","Harper Lee",24.95)

print(B1 == B3)
print(B1 == B4)
# print(B1 >= B3 )
# print(B4 < B2)

## TO MAKE THE INSTANCE SORTABLE
books= [B1,B3,B2,B4]
books.sort()
print([book.title for book in books])


##### MAGIC METHODS #####
#  __gt__(self, value)
#  __ge__(self, value)
#  __le__(self, value)
#  __lt__(self, value)