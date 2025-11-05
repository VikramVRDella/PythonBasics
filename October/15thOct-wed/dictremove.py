print(
    '''
    ***************************
    * Remove Dictionary Items *
    ***************************
    '''
)

print(
    '''
    ********************************
    * 1.Remove Item                *
    * 2.Remove Last Inserted Item  *
    * 3.Clear the Dictionary       *
    * 4.Delete the Dictionary      *
    * 5.Exit                       *
    ********************************
    '''
)
dict1={
    "name":"John",
    "age":32,
    "city":"NewYork"
}
print(dict1)
choice=int(input("Enter your Choice : "))

if choice==1:
    x=input("Enter the Item to remove : ")
    dict1.pop(x)
    print("Item Removed....")
    print(dict1)
elif choice==2:
    print("Wanna insert the Item....")
    y=input("Enter the Key : ")
    z=input("Enter the Value : ")
    dict1[y]=z
    print(dict1)
    cho=input("wanna remove the item (y/n) : ")
    if cho=='y':
        dict1.popitem()
        print(dict1)
    else:
        print("Goodbye...")
        exit()
elif choice==3:
    print("wanna Clear the Dictionary...")
    dict1.clear()
    print("Dictionary Cleared..")
    print(dict1)
elif choice==4:
    print("Wanna Delete A dictionary....")
    del dict1
    print("Dictionary Deleted...")
elif choice==5:
    print("Goodbye.....Thankyou")
    exit()
else :
    print("Choose the Correct Option....")
