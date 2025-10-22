print(
    '''
    ************************
    * Python Encapsulation *
    ************************
    '''
)
class Def:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age must be Positive.....")
            
obj=Def('John',25)
print(obj.name)
print("\n")
print("Accessing Private Variables....")
print(obj.get_age())
print("\n")
print("Setting Age....")
obj.set_age(26)
print(obj.get_age())
