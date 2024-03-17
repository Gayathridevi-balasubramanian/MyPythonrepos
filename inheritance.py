
class Dog:
    _legs = 4
    def __init__(self, name):  #initialization function
        self.name = name

    def getlegs(self):
        return self._legs 
       
    def speak(self):
        print(self.name + 'says : Bark!')
    
class chihuahua(Dog):
    _legs = 3 
    def speak(self):
        print(self.name + ' says : yap yap yap!')
    def wagTail(self):
        print('Vigorous wagging!')

dog = chihuahua('Roxy') #initiliaze using the child class
print(dog._legs)
print(dog.getlegs())
dog.speak()
dog.wagTail()

myDog = Dog('Rover') # initialixed using the parent class
print(myDog.getlegs())
myDog.speak()


## Extending the built in class like lists
myList = list() # list() here is a class not a function

class UniqueList(list):
    append = lambda self, item: super(UniqueList, self).append(item) if item not in self else None

myList = UniqueList()
myList.append(500)
myList.append(300)
myList.append(500) #UniqueList is not appending the values with duplicate values
print(myList)


## Extending the built in classes by overriding or extending the property
class UniqueList(list):
    append = lambda self, item: super(UniqueList, self).append(item) if item not in self else None

    def __init__(self):
        super().__init__()
        self.someProperty = " Unique lists property!"


myList = UniqueList()
myList.append(500)
myList.append(300)
myList.append(500) #UniqueList is not appending the values with duplicate values
print(myList)
print(myList.someProperty)
