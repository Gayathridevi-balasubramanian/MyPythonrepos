from abc import ABC , abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calArea(self):
        pass
class Jsonify(ABC):
    def __init__(self) :
        super().__init__()
    @abstractmethod
    def toJsonify(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calArea(self):
        return 3.14 * self.radius ** 2 
    def toJsonify(self):
        return f"{{'Çircle': {str(self.calArea())}}}"

        

class Square(GraphicShape):
    def __init__(self,side):
        self.side = side

    def calArea(self):
        return self.side * self.side

#g = GraphicShape()
c1 = Circle(23)
s1 = Square(15)
s1.calArea()
print(c1.toJsonify())
