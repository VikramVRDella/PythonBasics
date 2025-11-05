print(
    '''
    **********************
    *  Python Functions  *
    **********************
    '''
)

def func():
    print("Hello from Function!")
func()
func()
func()

print("Want to convert to Celsius")
def farenheit_to_celsius(farenheit):
    return(farenheit - 32)*5/9

faren=int(input("Enter the Farenheit : "))
print(farenheit_to_celsius(faren))

print("Return Values...")

def get_greating():
    return "Hello from Function...."

message=get_greating()
print(message)
    
def funct1():
    pass
funct1()
