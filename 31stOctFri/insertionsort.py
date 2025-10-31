def InsertionSort(arr):
    
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    
    return arr

list1=[]
n=int(input("Enter how many elements : "))
for i in range(n):
    element=int(input(f"Enter the {i+1} Element :"))
    list1.append(element)

print(f"Given Array : {list1}")
result=InsertionSort(list1)
print(f"Sorted Array : {result}")

