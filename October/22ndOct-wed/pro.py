print(
    '''
    ************************
    * Producted Properties *
    ************************
    '''
)
class Sample:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
obj=Sample("Linus",50000)
print(obj.name)
print(obj._salary)
print("\n")
print(
    '''
    *************************
    * Inner Class in Python *
    *************************
    '''
)

class Outer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    class Inner:
        def __init__(self):
            print("Inner Class")

obj1=Outer("Martin",23)
obj2=Outer.Inner()
obj2
print(obj1.name)
print(obj1.age)
