print(
    '''
    **************************
    * Polymorphism in Python *
    **************************
    '''
)

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail!")

obj1=Car("Toyoto","C20")
obj2=Boat("KingFisher","E321")

for x in(obj1,obj2):
    print(x.brand)
    print(x.model)
    x.move()
