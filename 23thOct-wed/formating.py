print(
    '''
    *********************
    * String Formatting *
    *********************
    '''
)
print("F-strings....")
txt=f"The price of bread is 49 Dollars"
print(txt)
print("\n")
print("F-strings with Variables...")
price=45
print(f"The price of Jam is {price} Dollars")
print(f"The price of Bread is {price:.2f} Dollars")
print("\n")
print("Perform Operations with F-Strings....")
print(f"The Multiplication of 20 and 50 is {20*50} ")
print("\n")
print("If-Else Condition on F-Strings....")
pri=int(input("Enter the Price : "))
print(f"It's Very {'Expensive' if pri>50 else 'cheap'}")
print("\n")
print("Execute Function on F-Strings.....")
fruits="apple"
print(f"It is a {fruits.upper()}")
print("\n")
print("User Defined Function....")
def myconvertor(x):
    return x*0.3048

print(f"The Flight is from {myconvertor(30000)} meters")
print("\n")
print(f"The price is {pri:,}")
