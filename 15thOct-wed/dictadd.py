print(
    '''
    *************************
    *  Add Dictionary Items *
    *************************
    '''
)

dict1={
    "name":"John",
    "age":32
}
print(dict1)
choice=input("Wanna add new elements in dictionary (y/n) : ")

if choice=='y':
    a=input("Enter the Key : ")
    b=input("Enter the Value : ")
    cho=input("Wanna use Update function (y/n) : ")
    if cho=='y':
        dict1.update({a:b})
        print(dict1)
    else:
        dict1[a]=b
        print(dict1)
else:
    print(dict1)
    print("Goodbye....Thankyou")
    
