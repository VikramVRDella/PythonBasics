print(
    '''
    **********************
    * Decorator Function *
    **********************
    '''
)

def casechange(func):
    def inner():
        return func().upper()
    return inner

@casechange
def myfunction():
    return "Hello Doe!!!!"

@casechange
def otherfunction():
    return "Hello John!!!!"

print(myfunction())
print(otherfunction())
print("\n")
print("Arguments with Decorated Function...")
def casechange1(func):
    def inner(x):
        return func(x).upper()
    return inner
@casechange1
def function3(name):
    return "Hello "+name
print(function3("John"))
print("Arguments *args and **kargs Function.....")
n=input("Enter the Name : ")
def casefunction(funct):
    def inner(*args,**kwargs):
        return funct(*args,**kwargs).upper()
    return inner

@casefunction
def Function(name):
    return "Hello "+name

print(Function(n))
print("\n")
print("Decorator with Arguments")
def ccasechange(n):
    def decorator(func):
        def inner():
            if n==1:
                a=func().upper()
            else:
                a=func.lower()
            return a
        return inner
    return decorator

@ccasechange(1)
def mfunc():
    return "Hello Joe"

print(mfunc())
