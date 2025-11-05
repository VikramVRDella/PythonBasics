print(
    '''
    *****************************
    * Functional *awrgs *kwargs *
    *****************************
    '''
)

def func1(greeting,*names):
    for name in names:
        print(greeting," ",name)

num=int(input("How many names : "))   
n=[]
for i in range(num):
    x=input("Enter the Names : ")
    n.append(x)
for i in range(num):
    func1("Hello",n[i])
print("\n")
print("Addition Arguments")
def addfun(*num):
    total=0
    for i in num:
        total+=i
    return total

a=int(input("Enter the Number : "))
b=int(input("Enter the Number : "))

message=addfun(a,b)
print(message)

print("\n")
print("Arbitary Keyword Arguments.....")

m=input("Enter the First Name : ")
n=input("Enter the Last Name : ")

def func(**kid):
    print(f"His First Name is "+kid["fname"]) 
    print("His last Name is "+kid["lname"])


func(fname=m,lname=n)
print("\n")
print("**kwargs with Regular Parameters....")
def func1(user,**details):
    print(f"Username : {user}")
    print("Additional Parameters....")
    for keys,values in details.items():
        print(" ",keys+" "+":",values)

username=input("Enter your Username : ")
func1(username,age=25,city="Newyork")
print("\n")
print("Combining *args and **kwargs and regular arguments....")
def funct2(title,*name,**details):
    print(f"Regular Arguments : {title}")
    print(f"Positional Arguments : ",name)
    print(f"Keyword Arguments : ",details)

tit=input("Enter the Title : ")
funct2(tit,"Emily","John",age=25,city="Newyork")
print("\n")
print("Unpacking Lists....")
def funcnum(a,b,c):
    return a+b+c

numbers=[1,2,3]
a=funcnum(*numbers)
print(a)
print("Unpacking Dictionaries...........")
def func3(fname,lname):
    print("Hello ",fname,lname)

person={
    "fname":"John",
    "lname":"Doe"
}
func3(**person)
