print(
    '''
    *******************
    *   Tuple Update  *
    *******************      
    '''
)

tuple1=["apple","ball","cherry"]
print("Before Updating...")
print(tuple1)
y=list(tuple1)
y[1]="kiwi"
tuple1=tuple(y)
print("After Updating...")
print(tuple1)


print("Appending in tuple")
y=("orange",)
tuple1+=y
print(tuple1)

y=list(tuple1)
y.append("kiwi")
tuple1=tuple(y)
print(tuple1)

print("Removing a Specific Item in a tuple")
y=list(tuple1)
print(tuple1)
ele=input("Enter the Element want to remove : ")
y.remove(ele)
print("Element Removed....")
tuple1=tuple(y)
print(tuple1)

print("Deleting operation")
del tuple1
print(tuple1)
