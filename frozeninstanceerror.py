''' with the frozen = true you can set value to the attributes 
      only during the initialization , but not during the processing'''

from dataclasses import dataclass
@dataclass(frozen=True)
class Immutable:
    value1 : str = "Value1"
    value2 : int = 0 

    def changevalue(self , values):
        self.value1 = values
        


# creating the oblects
im = Immutable()
obj = Immutable("another string", 45)

print(im.value1, im.value2)
print("obj with initialization: ",obj)

# # try changing the value
# im.value1 = "changed value"
# print(im.value1)

im.changevalue("dhgnlfd")
print(im.value1)