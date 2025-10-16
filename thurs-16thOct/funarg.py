print(
    '''
    **********************
    * Function Arguments *
    **********************
    '''
)

print("Function with One Arguments.....")
def function2(name):
    print(f"Hello {name}!!!")

n=input("Enter your name : ")
function2(n)
print("\n")
print("Function with Two Arguments.....")
def function3(fname,lname):
    print(f"Hello {fname} {lname}!!!")

n2=input("Enter your first Name : ")
n3=input("Enter your Second Name : ")

function3(n2,n3)
print("\n")
print("Function with Default Value....")
def function4(name="friend",city="NewYork"):
    print(f"Hello {name}")
    print(f"I am from {city}")

function4("Doe","Africa")
function4()
print("\n")
print("Function attributes with Key Value Pairs....")
def function5(animal,name):
    print(f"You have a {animal}")
    print(f"And Your {animal} name is {name}")
aname=input("Enter the animal Category : ")
n=input(f"Enter the Name of {aname} : ")
function5(animal=aname,name=n)
print("\n")
print("Mixing Arguments.....")

def fun6(animal,name,age):
    print(f"My {animal} name is {name} and age is {age} years old")

fun6("dog",name="Buddy",age=5)
print("\n")
print("Passing Different Datatypes.....")

def fun7(fruits):
    for x in fruits:
        print(x)

myfruits=["apple","banana","mango"]
fun7(myfruits)
print("\n")
print("Sending Dictionary as an Arguments....")
def fun8(persons):
    print("Name :",persons["name"])
    print("Age :",persons["age"])
my_persons={"name":"John","age":32}
fun8(my_persons)
print("\n")
print("Return Values...")
a=int(input("Enter the Number : "))
b=int(input("Enter the Number : "))

def addfun(x,y):
    return x+y

print(addfun(a,b))
print("\n")
def addfun1():
    return ["apple","banana","mango"]

message=addfun1()
print(message[0])
print(message[1])
print(message[2])
print("\n")
print("Positional Arguments Only...")
def fun9(name,/):
    print(f"Hello {name}")

nam="Doe"
fun9(nam)
print("\n")
print("Keyword Arguments Only.......")
def fun10(*,name):
    print(f"Hello {name}")
fun10(name="John")
print("\n")
print("Combining Positonal and Keyword Only arguments.....")
a=int(input("Enter Number : "))
b=int(input("Enter Number : "))
c=int(input("Enter Number : "))
d=int(input("Enter Number : "))

def fun11(x,y,/,*,z,k):
    return(f"{x+y} and {z+k}")
print(fun11(a,b,z=c,k=d))
