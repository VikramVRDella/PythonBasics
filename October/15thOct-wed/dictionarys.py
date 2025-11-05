print(
    '''
    ****************
    * Dictionaries *
    ****************
    '''
)

dict1={
    "name":"John",
    "age":23,
    "age":25
}
print(dict1)

print("Accessing from the Dict.......")
print(dict1['age'])
print(type(dict1))

print("Assigning Dictionaries using Constructors.....")
dict2=dict(name="Doe",age=27,country="Africa")
print(dict2)

print("Retriving using Get Method....")
x=dict2.get('age')
print(x)

print("Retriving Keys Only....")
y=dict2.keys()
print(y)


print("Wanna add the Key Value pair....")
acc1=input("Enter the key : ")
acc2=input("Enter the value : ")

dict2[acc1]=acc2
print("Element Added...")
print(dict2)

print("Retriving Values Only....")
z=dict2.values()
print(z)

print("Retriving Items in Dictionary")
a=dict2.items()
print(a)
