print(
    '''
    *************************
    * While Loop Statements *
    *************************
    '''
)

# While Loop Example
i=int(input("Enter the Number : "))

while i<6:
    print(i)
    i+=1

#Break while condition is true

j=int(input("Enter another Number : "))

while j<=10:
    print(j)
    if j==6:
        break
    j+=1

k=int(input("Enter another Number : "))

while k<=10:
    k+=1
    if k==6:
        continue
    print(k)

l=int(input("Enter another Number : "))

while l<=6:
    print(l)
    l+=1
else:
    print(f"{l} is no longer than 6")
