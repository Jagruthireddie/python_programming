from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of rectangle",self.l*self.b)
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of circle",3.14*self.r*self.r)
r=rectangle(10,20)
c=circle(5)
r.area()
c.area()