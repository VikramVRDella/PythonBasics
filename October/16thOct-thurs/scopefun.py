print(
    '''
    ******************
    * Function Scope *
    ******************
    '''
)
#Local Scope Variable : 
def func():
    x=300
    print(x)

func()
print("\n")
print("Function Inside a Function...")
def func1():
    x=300
    def innerfun():
        print(x)
    innerfun()

func1()
print("\n")
print("Global Scope Function....")
x=300
def fun2():
    print(x)
fun2()
print("\n")
print("Global and Local Scope Variables...")
x=200
def fun3():
    x=300
    return x
a=fun3()
print("Global Scope : ",x)
print("Local Scope : ",a)
print("\n")
print("Global Keyword....")
x=300
def fun4():
    global x
    x=400
    return x
b=fun4()
print(b)
print(x)
print("\n")
print("Non local Keyword....")
def funct2():
    x="John"
    def innerFun():
        nonlocal x
        x="Doe"
        print(x)
    innerFun()
    print(x)
    
funct2()
print("Understanding the Local,Enclosing,outer,Global......")
x="global"
def funct4():
    x="Enclosing"
    def inner():
        x="inner"
        print("Inner : ",x)
    inner()
    print("Outer : ",x)

funct4()
print("Global : ",x)
