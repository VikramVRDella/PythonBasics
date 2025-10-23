print(
    '''
    *****************
    * Pandas Series *
    *****************
    '''
)
import pandas as pd
a=[1,6,5]
myvar=pd.Series(a)
print(myvar)
print("\n")
print("Accessing a Specific Values....")
print(myvar[0])
print("\n")
print("Indexing the Series.....")
var=[1,5,2]
var_my=pd.Series(a,index=["x","y","z"])
print(var_my)
print("\n")
print("Key/Value Objects as Series.....")
calories={'day1':420, 'day2':320, 'day3':432}
data=pd.Series(calories)
print(data)
