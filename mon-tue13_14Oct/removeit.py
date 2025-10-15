list1=["apple","ball","cat","dog","elephant","dog"]
print(list1)
choice=input("Enter the element wanna remove : ")
print("Element Removed...")
list1.remove(choice)
print(list1)
#Remove Method will remove the item with more number of occurance, it will remove the first occurance
print("Remove Elements using Pop function")
cho=int(input("Enter the Index to pop : "))
list1.pop(cho)
print(list1)

print("Remove Elements using \"del\" function")
print("Wanna delete a element or the Entire list")
print(
    '''
    **********************
    * 1.Element Deletion *
    * 2.Entire List      *
    **********************
    '''
)
print(list1)
cho1=int(input("Enter the Choice : "))
if cho1==1:
    place=int(input("Enter the Index of the Element to del : "))
    del list1[place]
    print("Item Deleted...")
    print(list1)
else:
    del list1
    print("List Deleted...")

print("Using Clear Function")
list1.clear()
print("List Cleared...")

    
