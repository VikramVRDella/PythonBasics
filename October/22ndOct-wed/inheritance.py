print(
    '''
    **********************
    * Python Inheritance *
    **********************
    '''
)

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printName(self):
        print(self.firstname, self.lastname)

obj1=Person("John","Doe")
obj1.printName()
print("\n")
class Student(Person):
    pass
obj2=Student("Mike","Alvin")
obj2.printName()
print("\n")
print("Add __init__ function to child class...")
class Inheri:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Child(Inheri):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def __str__(self):
        return f"{self.name} {self.age} {self.rollno}"
        
a=input("Enter Student Name : ")
b=int(input("Enter Student age : "))
c=int(input("Enter Student RollNo : "))

obj3=Child(a,b,c)
print(obj3)        
print("\n")
print("Adding New Properties....")
class Geo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Stato(Geo):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.graduation=2019

obj4=Stato("Mike",23)
print(obj4.graduation)

class Fred:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Profd(Fred):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.graduation=year
    def welcome(self):
        print(f"Hello {self.name} {self.age} to the class of {self.graduation}")

obj5=Profd('George','Milton',2019)
obj5.welcome()
