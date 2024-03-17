# to implement multiple inheritance
class A:
    def __init__(self) :
        super().__init__()
        self.prop1 = "Prop1"
        self.name = "ClassA"

class B:
    def __init__(self) :
        super().__init__()
        self.prop2 = "Prop2"
        self.name = "ClassB"

class C(A,B):
    def __init__(self) :
        super().__init__()

    def get_properties(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

c1 = C()
c1.get_properties()

'''  the name attribute is the common attribute found in both the base classes 
      when the name attribute is called it first looks inthe child classes 
      when it is not defined in the child classes then 
                      it looks into the base classes from left to right inthe 
                                      it is defined in the declaration
                                                      ex: C -> A -> B  
        THIS CAN BE KNOWN BY USING THE "MRO" Method Resolution Order   '''

print(C.__mro__) 
