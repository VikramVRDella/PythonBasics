def LinearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        
    return -1

list1=list(range(1,21))

value=int(input("Enter the Value to found  : "))

result=LinearSearch(list1,value)

if result!=-1:
    print(f"Element Found at {result}")

else:
    print("Element not Found")
