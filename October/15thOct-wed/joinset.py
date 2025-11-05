print(
    '''
    ********************
    *    Join Sets     *
    ********************
    '''
)

print("Union Operation")
set1={"apple","ball","cat","dog"}
set2={1,4,5,3,2}
set3=set1.union(set2)
print(set3)

print("Union Operator using \"|\" Operator")
set4=set1|set2 # Uses only to unite only the similar sets
print(set4)

print("Joining Multiple Sets")
set5={"anaconda","bat","cricket","doll"}
set6={23,12,43,645}
set7=set1.union(set2,set5,set6)
print(set7)

print("Union Operator using \"|\" Operator")
set8=set1|set2|set5|set6
print(set8)

print("Joining a Set and Tuple")
tuple1=("Dog","Ball","Cat")
set9=set8.union(tuple1)
print(set9)

print("Using Update Function...")
set8.update(set1)
print(set8)

print("Intersection Operator...")
set11={"apple","google","amazon"}
set12={"apple","banana","grapes"}
set14=set11.intersection(set12)
print(set14)

print("Intersection Operator using \"&\" Operator")
set15=set11&set12
print(set15)

print("Using Intersection_update Function....")
# set11.intersection_update(set12)
# print(set11)

print("Using Difference Operator....")
set16=set11.difference(set12)
print(set16)

print("Intersection Operator using \"-\" Operator")
set17=set11-set12
print(set17)

print("Difference Update Operation.....")
set11.difference_update(set12)
print(set11)

print("Symmetric Differences......")
set18=set11.symmetric_difference(set12)
print(set18)

print("Intersection Operator using \"^\" Operator")
set19=set11^set12
print(set19)

set20={"apple","ball","cat"}
set21={"apple","dog","anaconda"}

print("Symmetric Difference Update operation.........")
set20.symmetric_difference_update(set21)
print(set20)
