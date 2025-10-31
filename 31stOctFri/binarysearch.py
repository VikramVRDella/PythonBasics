def BinarySearch(arr,key):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==key:
            return mid
        
        if arr[mid] < key:
            left=mid+1
        else:
            right=mid-1
    return -1

list1=list(range(1,100))
value=int(input("Enter the Value to Found : "))

result=BinarySearch(list1,value)

if result!=-1:
    print(f"Element found at the place of {result}")
else:
    print("Element not Found....")