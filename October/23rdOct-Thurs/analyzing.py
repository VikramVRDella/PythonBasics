print(
    '''
    *************************
    * Pandas Analyzing Data *
    *************************
    '''
)
import pandas as pd
df=pd.read_csv("sample.csv")
print(df.head(10))
print("\n")
print("Returning Last 5 rows....")
print(df.tail())
print("\n")
print("Printing Data Info.....")
print(df.info())
