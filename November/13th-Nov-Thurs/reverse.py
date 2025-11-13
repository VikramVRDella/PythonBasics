print(
    '''
    ********************
    * Reverse a String *
    ********************
    '''
)

string=input("Enter the String : ")

def reversed(s):
    return s[::-1]

print(f"Entered String : {string}")
print(f"Reversed String : {reversed(string)}")
