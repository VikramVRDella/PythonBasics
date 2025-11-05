print(
    '''
    **************************
    *   List Comprehension   *
    **************************
    '''
)

list1=["apple","banana","mango","cherry"]
newlist=[]


for x in list1:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlist1=[x for x in list1 if x!="apple"]
print(newlist1)
newlist2=[x for x in range(10)]
print(newlist2)
newlist3=[x for x in range(10) if x>5]
print(newlist3)

newlist4=[x.upper() for x in list1]
print(newlist4)
