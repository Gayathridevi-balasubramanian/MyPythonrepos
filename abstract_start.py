from abc import ABC , abstractmethod
# WITHOUT ABSTRACTION
# class GraphicShape:
#     def __init__(self):
#         super().__init__()
#     def calArea(self):
#         pass

# class Circle(GraphicShape):
#     def __init__(self, radius):
#         self.radius = radius

# class Square(GraphicShape):
#     def __init__(self,side):
#         self.side = side

# g = GraphicShape()
# c1 = Circle(23)
# s1 = Square(15)
# s1.calArea()


# WITH ABSTRACTION CLASSES

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calArea(self):
        return 3.14 * self.radius ** 2 

class Square(GraphicShape):
    def __init__(self,side):
        self.side = side

    def calArea(self):
        return self.side * self.side

#g = GraphicShape()
c1 = Circle(23)
s1 = Square(15)
s1.calArea()

