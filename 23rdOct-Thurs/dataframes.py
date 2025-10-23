print(
    '''
    ********************
    * Pandas DataFrame *
    ********************
    '''
)
import pandas as pd

data={
    'calories':[430,340,432,765],
    'duration':[40,20,32,21]
}
df=pd.DataFrame(data)
print(df)
print("\n")
print("Locating Row....")
print(df.loc[0])
print("\n")
print("Locating Row and Column....")
print(df.loc[[0,1]])
print("\n")
print("Naming Indexes...")
df1=pd.DataFrame(data,index=['day1','day2','day3','day4'])
print(df1)
print("\n")
print("Locating with the Index in dataframes......")
print(df1.loc['day1'])
