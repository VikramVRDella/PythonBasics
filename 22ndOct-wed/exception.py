print(
    '''
    *********************
    * Exception Raising *
    *********************
    '''
)

a=int(input("Enter any Number : "))

if a<0:
    raise Exception("Sorry, No negative Numbers....")
else:
    print(f"Entered Number is {a}")
