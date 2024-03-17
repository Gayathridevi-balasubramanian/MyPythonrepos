class Dog:
    def __init__(self, name):  #initialization function
        self.name = name
        self.legs = 4
    def speak(self):
        print(self.name + 'says : Bark!')
    

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

# class attributes can be called directly by the class itself
# print(Dog.legs)


class Dog:
    legs = 4
    def __init__(self, name):  #initialization function
        self.name = name
       
    def speak(self):
        print(self.name + 'says : Bark!')

# class attributes can be called directly by the class itself
print(Dog.legs)

Dog.legs = 3
print(Dog.legs)

#
class Dog:
    _legs = 4
    def __init__(self, name):  #initialization function
        self.name = name
    def getlegs(self):
        return self._legs 
       
    def speak(self):
        print(self.name + 'says : Bark!')
myDog = Dog('Rover')
Dog.legs = 3
print(f'this is modified class {Dog._legs}')
print(myDog.getlegs())


class Dog:
    _legs = 4
    def __init__(self, name):  #initialization function
        self.name = name
    def getlegs():  # there is no self keyword mentioned here
        return Dog._legs 
       
    def speak(self):
        print(self.name + 'says : Bark!')
        myDog = Dog('Rover')
Dog.legs = 3
print(f'this is modified class {Dog.legs}')
# myDog = Dog('Rover') # gives error bcz the myDog.getlegs() refers to the another myDog before
print(myDog.getlegs())
print(Dog.getlegs())


class Dog:
    _legs = 4
    def __init__(self, name):  #initialization function
        self.name = name
    def getlegs(self): 
        return self._legs 
       
    def speak(self):
        print(self.name + 'says : Bark!')
        myDog = Dog('Rover')

        Dog.legs = 3
print(f'this is modified class {Dog._legs}')
myDog = Dog('Rover') # gives error bcz the myDog.getlegs() refers to the another myDog before
print(myDog.getlegs()) # this instance refers to the instance of the class.
print(Dog._legs) # this refers to the attributes in class
print(myDog._legs)
myDog._legs = 3 
print(Dog._legs) # this refers to the attributes in class so bring the class value
print(myDog._legs) # this refers to the attributes in the instance and shows the modified value of the instance
