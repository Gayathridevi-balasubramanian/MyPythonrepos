class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = [] 
    def addchapter(self,chapter ):
        self.chapters.append(chapter)

    def get_pagecount(self):
        result = 0 
        for ch in self.chapters:
            result += ch.pagecount               # chapters has two attributes in the list so it is necessary to ch.pagecount
        return result
        
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

class Author:
    def __init__(self,fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"{self.fname }{ self.lname}"


author = Author("Leo","Tolstoy")
b1 = Book("War and Peace",29.0,author)

b1.addchapter(Chapter("chapter1", 300))
b1.addchapter(Chapter("chapter2", 234))
b1.addchapter(Chapter("chapter3", 234))

print(b1.author)
print(b1.get_pagecount())
'''  COMPOSITION - is calling the class as a parameter in another class to show the relationship of the class in the base class
The class is called in the mainclass to represent the data of the another class with limited details      '''