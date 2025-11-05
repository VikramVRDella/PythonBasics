print(
    '''
    *******************
    * Init Statements *
    *******************
    '''
)
class Sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=input("Enter your Name : ")
b=int(input("Enter your age : "))
p1=Sample(a,b)
print(f"Your name is {p1.name} and your age is {p1.age}")
print("\n")
print("Class without Init")
class Person:
    pass
p1=Person()
p1.name="Thomas"
p1.age=21
print(p1.name)
print(p1.age)
print("\n")
print("Default Value in __init__  method")
class Def:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age

obj1=Def(a,b)
obj2=Def(a)
print(f"{obj1.name} {obj1.age}")
print(f"{obj2.name} {obj2.age}")
print("\n")
print("Multiple Arguments....")
class Sam:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city= city
        self.country=country

na=input("Enter your Name :")
ag=int(input("Enter your age :"))
ci=input("Enter your city :")
co=input("Enter your Country :")

obj3=Sam(na,ag,ci,co)
print(f"{obj3.name} {obj3.age} {obj3.city} {obj3.country}")
