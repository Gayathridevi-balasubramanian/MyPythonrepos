class Book:
    # property defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")
    __booklist = None
    # double underscore properties are hidden from other classes

    # create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    # create a static method
    @staticmethod 
    def get_book_lists():
        if (Book.__booklist == None ):
            Book.__booklist = []
        return Book.__booklist
    def set_title(self, newtitle):
        self.title = newtitle
    def  __init__(self,title, booktypes):
        self.title = title
        if( booktypes not in Book.BOOK_TYPES):
            raise ValueError(f"{booktypes} not a valid booktype")
        else:    
            self.booktypes = booktypes

b1 = Book("The Wings Of Fire","HARDCOVER")
# B2 = Book("THE GIFTS OF INDIA","HISTORY")  # THIS WOULD CREATE AN ERROR
B3 = Book("The gifts of India","PAPERBACK")
print(b1.BOOK_TYPES)
print(b1.get_book_types())
print(Book.get_book_types())

# trying to append the elements to the list and print
# first number is given and the b1 and B3 objects are added to the lists
booklists = Book.get_book_lists()
booklists.append(34)
booklists.append(b1)
booklists.append(B3)
print(booklists)