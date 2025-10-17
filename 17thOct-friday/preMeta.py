print(
    '''
    ***********************
    * Preserving Metadata *
    ***********************
    '''
)

def function1():
    return "Hello from Function...."

print(function1.__name__)
print("\n")
print(
    '''
    **********************
    * Decorated Function *
    **********************
    '''
)
def changecase(func):
    def inner():
        return func.upper()
    return inner

@changecase
def function2():
    return "Hello from function"

print(changecase.__name__)
print("\n")
print(
    '''
    ***********************************
    * Using functools.wrap() function *
    ***********************************
    '''
)
import functools

def casechange(func):
    @functools.wraps(func)
    def inner():
        return "Hello from Function...."
    return inner

@casechange
def function3():
    return "Have a Good Day!!!!"

print(casechange.__name__)
print("\n")
