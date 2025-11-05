print(
    '''
    *********************
    * Classes in Python *
    *********************
    '''
)

class Func:
    x=5

obj1=Func
print(obj1.x)
print("\n")
class Fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color

fruits=Fruits(name="Apple",color="red")
print(fruits.name)
print("\n")
class Students():
    def __init__(self,roll,name,age,marks):
        self.roll=roll
        self.name=name
        self.age=age
        self.marks=marks

    def __str__(self):
        return f"Roll no :{self.roll}, Name : {self.name}, Age:{self.age}, marks:{self.marks}"

print(
    '''
    ********************
    * Student Registry *
    ********************
    '''
)
n=int(input("Enter How many Students do you want to register : "))

stu=[]
for i in range(n):
    print("*************************")
    print(f"Enter Student {i+1} Details...")
    rol=int(input("Enter the Roll Number : "))
    nam=input("Enter the Name : ")
    ag=int(input("Enter the age : "))
    mar=int(input("Enter the Marks : "))
    print("*************************")
    print("\n")
    s=Students(roll=rol,name=nam,age=ag,marks=mar)
    stu.append(s)
print("\n")
print("Registered Students....")
for students in stu:
    print(students)
