# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price


# B1 = Book("War and peace","Loe Tolstoy", 23.56)
# B2 = Book("The catcher in the rail ","JD Sailgerr", 56.76 )

# print(B1)
# print(B2)

# using the __str__ and __repr__ magic functions
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


B1 = Book("War and peace","Loe Tolstoy", 23.56)
B2 = Book("The catcher in the rail ","JD Sailgerr", 56.76 )

print(B1)
print(B2)
print(str(B1))
print(repr(B2))

