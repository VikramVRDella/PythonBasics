print(
    '''
    ************************
    *    Sorting List      *
    ************************
    '''
)

animals=["Dog","Bull","elephant","dinosurs","anaconda"]
numbers=[10,40,15,35,95,82,75,56]

print("Ascending Order Sorting")
animals.sort()
print(animals)
numbers.sort()
print(numbers)
print("Reverse Sorting")
animals.sort(reverse=True)
print(animals)
numbers.sort(reverse=True)
print(numbers)

print("Customized Sorting")
def funsort(n):
    return abs(n-20)

numbers.sort(key=funsort)
print(numbers)

print("Case Insensitive")
animals.sort(key=str.lower)
print(animals)

print("Reverse Sorting")
animals.reverse()
print(animals)
