print(
    '''
    *******************
    *    FrozenSet    *
    *******************
    '''
)

x=frozenset({"apple","ball","cat"})
print(x)
print(type(x))

print("Copy Frozenset...")
y=x.copy()
print(y) #Shallow Copy only exists

print("Difference in Frozenset....")
froset1=frozenset({1,2,3,4})
froset2=frozenset({2,3,4})
froset3=froset1.difference(froset2)
froset4=froset1-froset2
print(froset3)
print(froset4)

print("Intersection in Frozenset....")
froset5=froset1&froset2
print(froset5)

print("Using Isdisjoint function.....")
print(froset1.isdisjoint(froset2))

print("Using Subset function.........")
print(froset1.issubset(froset2))

print("Using Superset function.........")
print(froset1.issuperset(froset2))

print("Using Symmetric Difference......")
froset6=froset1.symmetric_difference(froset2)
print(froset6)

print("Union in Frozenset....")
froset7=froset1|froset2
print(froset7)
