print(
    '''
    **********************
    * List Concatenation *
    **********************
    '''
)

print("Using\"+\" Operator")
list1=["apple","ball","cherry","dog"]
list2=[1,2,3,4,5]
list3=list1+list2
print(list3)

print("Using append function")
for x in list2:
    list1.append(x)

print(list1)

print("Using Extend function")
list1.extend(list2)
print(list1)
