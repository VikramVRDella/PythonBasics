print(
    '''
    ************************
    *   Add Item in Sets   *
    ************************
    '''
)

print("Adding Elements....")
sets={"apple","mango","kiwi"}
sets.add("orange")
print(sets)

print("Adding Two Sets")
set1={"dog","cat","elephant","ant"}
set2=sets
set1.update(set2)
print(set1)

print("Adding List and Set")
list1=["cat","ant","dog","anaconda"]
set2.update(list1)
print(set2)

print("Remove Operation from the Set")
#Remove method will raise the error so we can use the discard method
set2.discard("cat")
print(set2)

#pop will randomly pop the element from the set
set2.pop()
print(set2)

set2.clear()
print(set2)

del set2
# print(set2)
print("Set is deleted")
