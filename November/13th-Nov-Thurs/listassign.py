print(
    '''
    ***********************
    * List Initialization *
    ***********************
    '''
)

list1=[]

while True:
    ele=input("Enter the Element : ")
    if bool(ele) == False:
        break
    list1.append(int(ele))

print(f"Given Input : {list1}")
