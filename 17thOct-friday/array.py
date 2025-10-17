print(
    '''
    *********************
    *   Python Arrays   *
    *********************
    '''
)
fruits=["apple","grapes","banana"]
print(fruits)
print("\n")
print("Accessing the Array Elements......")
print(fruits[0])
print("\n")
print("Want to Change the Array Elements.....")
a=int(input("Enter the Elements Number : "))
ele=input("Enter the Element Name : ")
fruits[a]=ele
print("Element Changed....")
print(fruits)
print("\n")
print("Length of the Array")
print(len(fruits))
print("\n")
print("Printing Array Elements with for loop")
for i in fruits:
    print(i)
print("\n")
print("Appending an array...")
a=input("Enter an Element to append : ")
fruits.append(a)
print(fruits)
print("\n")
print("Remove Method....")
fruits.pop(0)
print(fruits)
f=input("Enter the Element to remove : ")
fruits.remove(f)
print(fruits)
