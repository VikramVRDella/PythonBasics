print(
    '''
    ***************************
    * Change Dictionary items *
    ***************************
    '''
)

dict1={
    "name":"John",
    "age":32,
    "city":"Newyork"
}

print(dict1)
choice=input("Wanna change in Dictionary item (y/n)")
if choice=='y':
    a=input("Enter the key :")
    b=input("Enter the Value : ")
    cho=input("wanna use update function(y/n) : ")
    if cho=='y':
        dict1.update({a:b})
    else:
        dict1[a]=b
    print(dict1)
else:
    print("Goodbye...ThankYou")
