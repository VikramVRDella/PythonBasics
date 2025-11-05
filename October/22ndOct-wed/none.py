print(
    '''
    *******************
    *   None Types    *
    *******************
    '''
)
x=None
print(x)
print(type(x))
print("\n")
print("Comparing Using NoneType....")
result=None
if result is None:
    print("The Result is None...")
else:
    print("The Result is Ready....")
print("\n")
print("Function Returning None....")
def func():
    x=5
fun=func()
print(fun)
