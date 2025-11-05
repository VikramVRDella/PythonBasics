print(
    '''
    ******************
    *  List Copy     *
    ******************
    '''
)

print("Using Copy Method...")
list1=["apple","ball","cheery","dog"]
newlist=list1.copy()
print(newlist)

print("Using List Method...")
newlist1=list(list1)
print(newlist1)

print("Using Slice Operator...")
newlist2=list1[:]
print(newlist2)
