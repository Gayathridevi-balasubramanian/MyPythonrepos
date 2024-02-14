## basic class definition
class Book:
    def __init__(self , title, author , pages, prices):
        ## add attributes : when in the init then it is called the instance attribute
        self.title = title
        self.author = author 
        self.pages = pages
        self.prices = prices
        self.__secret = "This is the secret information" 
# __ show that the attribute is only used within the class and called only as _Book__secret
    def getprices(self):
        if hasattr(self ,"_a" ):
            return self.prices - (self.prices * self._a / 100)
        else:
            return self.prices
    
    def setdiscount(self , percentage):
        self._a  = percentage
        
        
# create instance 
book1 = Book("Wings Of Fire" , "Abdul Kalam " , 500 , 100)
book2 = Book("Programming with python" , "Gayathri " , 608 , 80)

#print class and the property
print(book1)
print(book1.title)
print(book2.title)
print(book1.getprices)  # gives the details about the objects
print(book1.getprices())
print(book1.prices)
print(book2.setdiscount(0.05))
print(book2.getprices())
print(book2.setdiscount(55))
print(book2.getprices())

# ctrl+/   for adding comments to multiple lines


#print(book1.__secret)
# no attribute error

print(_Book__secret)

