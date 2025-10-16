print(
    '''
    ************************
    *  For Loop Statements *
    ************************
    '''
)

list1=["apple","banana","mango"]

for x in list1:
    print(x)

print("for loop with break statements aftr print....")

for x in list1:
    print(x)
    if x=="banana":
        break
    
print("for loop with break statements before print....")

for x in list1:
    if x=="banana":
        break
    print(x)

print("Using Continue Statements.....")

for x in list1:
    if x=="banana":
        continue
    print(x)

print("Using range in for loop.....")

for x in range(6):
    print(x)

print("Using range with starting and ending........")

for x in range(2,10):
    print(x)

print("Using range with starting and ending with sequence")

for x in range(1,30,3):
    print(x)

print("Using for with else statement")
for x in range(1,6):
    print(x)
else:
    print("Finished.......")

print("Nested Loops....")
list1=["apple","mango","orange"]
list2=["red","big","sweet"]

for x in list2:
    for y in list1:
        print(x,y)
print("pass Statement......")

for x in [0,1,2]:
    pass
