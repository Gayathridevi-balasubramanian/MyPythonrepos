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
from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.12

    def __str__(self):
        return f"{self.title} by author {self.author} , costs {self.price}"
    
    # def __repr__(self):
    #     return f"title = {self.title}, author = {self.author} , costs= { self.price}"
    
    def __getattribute__(self, name: str) :
        if (name == "price"):
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d )
        return super().__getattribute__(name)
    
        
    def __setattr__(self, name: str, value: Any):
        if name == "price":
            if (type(value)) is not float:
                raise valueError("The Price must be Float!")
        return super().__setattr__(name, value)
        
    # this method is executed when the method is not in the getattribute function
    def __getattr__(self,name):
        return name+"is not here ! "
    



B1 = Book("War and peace","Loe Tolstoy", 23.56)
B2 = Book("The catcher in the rail ","JD Sailgerr", 56.76 )

B1.price = 40.0
print(B1)

B1.price = float(89)
print(B1)


