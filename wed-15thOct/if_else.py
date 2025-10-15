print(
    '''
    **********************
    * if-else Statements *
    **********************
    '''
)
print("Wanna find Greatest Number...")

a=int(input("Enter the first Number : "))
b=int(input("Enter the Second Number : "))
c=int(input("Enter the Third Number : "))

if a>b & a>c:
    print(f"{a} is greater than {b} & {c}")
elif b>a & b>c: 
    print(f"{b} is greater than {a} & {c}")
else:
    print(f"{c} is greater than {a} & {b}")

print("Short-Hand if-else statement.....")

a1=int(input("Enter the first Number : "))
b1=int(input("Enter the Second Number : "))

print(f"{a1} is greater than {b1}") if a1>b1 else print(f"{b1} is greater than {a1}")


print("Using And Operator.....")
x=int(input("Enter x :"))
y=int(input("Enter y :"))
z=int(input("Enter z :"))

if x>y and x>z:
    print("Both the conditions are true")
elif x>y or x>z:
    print("One of the condition is True")

l=30
m=40
if not l>m:
    print(f"{l} is not greater than {m}")
