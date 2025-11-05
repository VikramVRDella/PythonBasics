import math
print(
    '''
    ************************
    * User Input Functions *
    ************************
    '''
)

a=input("Enter your Name : ")
print(f"Hello {a}")
print("\n")
print("Getting Multiple Inputs....")
f1=input("Enter your Favorite thing : ")
f2=input("Enter your Favorite color : ")
f3=input("Enter your Favorite number : ")
print(f"Do you want a {f3} {f2} {f1} ?")
print("\n")
print("Entering Square Root by Getting Input....")
z=input("Enter the Number : ")
b=math.sqrt(float(z))
print(f"The Square Root of {z} is {b}")
print("\n")
print("Getting Input Until it Gets True")
y=True
while y==True:
    x=input("Enter the Number :")
    try:
        x=float(x)
        y=False
    except:
        print("Something went Wrong....")

print("Thank You...")
        
