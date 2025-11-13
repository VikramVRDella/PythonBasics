print(
    '''
    ********************
    * Change List Item *
    ********************
    '''
)

list1=[]

for i in range(5):
    ele=int(input(f"Enter the {i+1} Element : "))
    list1.append(ele)

print(f"List is {list1}")

index=int(input("Enter the Index to Change : "))
replace=int(input("Enter the Element to replace : "))

# list1[index-1]=replace
list1.insert(index-1,replace)
print(f"Replaced List is {list1}")
