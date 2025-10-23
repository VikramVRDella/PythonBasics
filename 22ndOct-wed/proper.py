print(
    '''
    ********************
    * Class Properties *
    ********************
    '''
)

class Sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Sample("Linus",30)
print(p1.name)
print(p1.age)
print("\n")
print("Modifing Properties...")
p1.age=45
print(f"Modified age :{p1.age}")
print("\n")
print("Deleting Property...")
del p1.age
# print(p1.age)
print("\n")
print("Class and Object Properties....")
class Sample2:
    lastname="Torvalds"
    def __init__(self,name):
        self.name=name

obj1=Sample2("Richard")
obj2=Sample2("Tom")
print(obj1.name)
print(obj2.name)
print(obj1.lastname)
print(obj2.lastname)
print("\n")
print("Modifying Class Properties....")
class Sample3:
    lastname=""
    def __init__(self,name):
        self.name=name
        # self.age=age
obj3=Sample3("Martin")
obj4=Sample3("Richard")

Sample3.lastname="Luther"
print(obj3.name)
print(obj3.lastname)

print(obj4.name)
print(obj4.lastname)
print("\n")
print("Adding Properties....")
obj3.age=21
obj3.city="NewDelhi"
print(obj3.age)
print(obj3.city)
