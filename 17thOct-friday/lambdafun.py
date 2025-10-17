print(
    '''
    *******************
    * Lambda Function *
    *******************
    '''
)

print("Addition using Lambda Functions...")
a=int(input("Enter the Number : "))
b=int(input("Enter the Second Number : "))
add=lambda x,y :x+y
print(add(a,b))
print("\n")
print("Multiply using Lambda Functions......")
c=int(input("Enter the Number : "))
d=int(input("Enter the Second Number : "))
mul=lambda l,m:l*m
print("Multiplication is",mul(c,d))
print("\n")
print("Summarize using Lambda Function....")
e=int(input("Enter the Number : "))
f=int(input("Enter the Another Number : "))
g=int(input("Enter the Another Number : "))
sum1=lambda s,f,g : s+f+g
print(f"Summarize of {e}, {f}, {g} is :",sum1(e,f,g))
print("\n")
print("Defining Lambda Inside a Function.....")
h=int(input("Enter the Number : "))
i=int(input("Enter the Another Number : "))
def function1(n):
    return lambda a : a*n

anovar=function1(h)
print(anovar(i))
print("\n")
print("Multiple Substitutions....")
j=int(input("Enter the Number : "))
k=int(input("Enter the Another Number : "))
l=int(input("Enter the Another Number : "))
def function2(n):
    return lambda a:a*n
mydouble=function2(j)
mytripler=function2(k)
print(mytripler(l))
print(mydouble(l))
print("\n")
print("Lambda Functions with Default Functions...")
list1=[1,32,2,4,5,6]
doubled=list(map(lambda x:x*2,list1))
print(doubled)
print("\n")
print("Using Filter() function....")
numbers=[1,2,3,4,5,6,7]
even=list(filter(lambda x:x%2==0,numbers))
print(even)
print("\n")
print("Using Sorted Function....")
stu=[("Emily", 25), ("John",22),("George",23)]
sort=sorted(stu,key=lambda x:x[1])
print(sort)
