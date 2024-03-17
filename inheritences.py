class Publisher:
    def __init__(self,title, price):
        self.price = price
        self.title = title

class Periodical(Publisher):
    def __init__(self, title , price, publisher , period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period  = period

class Book(Publisher):
    def __init__(self, author, pages, title, price):
        super().__init__(title, price)
        self.author = author
        self.pages  = pages

class Magazine(Periodical):
    def __init__(self, title , price, publisher , period):
        super().__init__(title, price, publisher , period)
        

class Newspaper(Periodical):
    def __init__(self, publisher, title, price , period):
        super().__init__(title, price , publisher , period)
        


b1 = Book("The Wings of fire","Abdul Kalam", 456, 23.45)
n1 = Newspaper("The Times Of India", "The New Times Company", 234, "daily")
m1 = Magazine("Science Fiction",346.40, "Sringer Nature","weekly")

print(b1.author)
print(n1.publisher)
print(m1.period , m1.price , m1.title)