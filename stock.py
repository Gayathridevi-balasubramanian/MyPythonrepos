from abc import ABC , abstractmethod

class asset(ABC):
    def __init__(self, price):
        self.price = price
    @abstractmethod
    def get_description(self):
        pass

class Bond(asset):
    def __init__(self,description,duration, yields,price):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yields = yields

    def __lt__(self, value):
        if not isinstance(value, Bond):
            raise ValueError("the object instance doesn't belong to the book")
        return (self.price < value.price)
    
    def __str__(self):
       return f"{self.description} : {self.duration} -- ${self.price}"

    def get_description(self):
        pass

class Stock(asset):
    def __init__(self, ticker, price ,company):
        self.ticker = ticker
        super().__init__(price)
        self.company = company
        # greater than equal to 

    def __lt__(self, value):
        if not isinstance(value, Stock):
            raise ValueError("the object instance doesn't belong to the book")
        return (self.price < value.price)

    def get_description(self):
        print(f"{self.ticker} : {self.company} -- ${self.price}")
stock = Stock("stidn", 34.4, "ABC.BV")
stock.get_description()
bond = Bond("the description", 23.45, 50, 45.76)
bond.get_description()

bonds = [ Bond(95.31, " 30 year US Treasury", 30 , 4.38),
         Bond(96.70, " 10 year US Treasury", 30 , 4.28),
         Bond(99.31, " 5 year US Treasury", 30 , 4.43),
         Bond(95.31, " 30 year US Treasury", 30 , 4.38)]

bonds.sort()
for b in bonds:
    print(b)

print(bonds)