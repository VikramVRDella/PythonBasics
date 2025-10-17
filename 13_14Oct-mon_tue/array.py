print(
    '''
    ********************
    * List Operations  *
    ********************
    '''
)

list1=["apple","ball","cat"]
print(list1)

list2=["apple",32,"ball",64,128]
print(list2)

# print(
#     '''
#     ******************
#     * Accessing List *
#     ******************
#     '''
# )
# 
list3=["apple","ball","cat","dog"]
# print("Enter the Elements you want to access")
# b=int(input("From : "))
# a=int(input("To : "))
# print(list3[b:a])


# print(
#     '''
#     ***********************
#     * Wana Check the List *
#     ***********************
#     '''
# )
# 
# a=input("Enter the name of the element do you want to check : ")
# if a in list3:
#     print(f"{a} in the Given List")
# else:
#     print(f"{a} not in the Given List")


print(
    '''
    ***************************
    * Wana Change the Element *
    ***************************
    '''
)

b=input("Enter a element you want to change : ")
c=input("Enter the new element you want to insert :  ")

if b in list3:
    print(f"{b} is Available")
    d=list3.index(b)
else:
    print(f"{b} is not Available")
list3.insert(d,c)
print(list3)
