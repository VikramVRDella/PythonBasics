list1=[4,2,1,5,7,9,8]
n=len(list1)

def BubbleSort(arr):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr

print(f"Given array : {list1}")
result=BubbleSort(list1)
print(f"Sorted Array : {result}")
