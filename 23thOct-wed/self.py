print(
    '''
    *************************
    * Python Self Parameter *
    *************************
    '''
)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello {self.name}")

obj1=Person("Linus",30)
obj1.greet()
print("\n")
print("Entering Name of the Persons")
class Sample:
    def __init__(self,name):
        self.name=name
    def printName(self):
        print(self.name)

a=input("Enter Name :")
b=input("Enter another Name :")
obj2=Sample(a)
obj2.printName()
obj3=Sample(b)
obj3.printName()
print("\n")
print("Without Using name self")
class Sample1:
    def __init__(myobj,name,age):
        myobj.name=name
        myobj.age=age
    def greet(obj):
        print(f"Hello {obj.name}")

obj3=Sample1("linus",30)
obj3.greet()
print("\n")
print("Accessing Properties with self....")
class Sample2:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def printModels(self):
        print(f"{self.brand} {self.model} {self.year}")
obj4=Sample2("Toyoto","C20",2023)
obj4.printModels()
print("\n")
print("Accessing Self within more than one function....")
class Sample3:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return "Hello " +self.name
    def welcome(self):
        message=self.greet()
        print(message+" Welcome to Our Website")

obj5=Sample3(a)   
obj5.welcome()
