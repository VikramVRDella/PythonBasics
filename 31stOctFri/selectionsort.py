def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

list1=[9,2,3,4,5,1,8,6]
print(f"Given Array : {list1}")

result=SelectionSort(list1)
print(f"Sorted Array : {result}")