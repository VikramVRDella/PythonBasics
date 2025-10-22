print(
    '''
    *******************
    * Python Classes  *
    *******************
    '''
)
class Func:
    x=5

p1=Func()
print(p1.x)
print("\n")
print("Creating Multiple Objects")
p2=Func()
p3=Func()
p4=Func()
print(p2.x)
print(p3.x)
print(p4.x)
print("\n")
print("Deleting Objects....")
del p4
print(p4.x)
print("Pass Statements.....")
class Sample:
    pass
