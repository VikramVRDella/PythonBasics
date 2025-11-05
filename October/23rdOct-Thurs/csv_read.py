print(
    '''
    ********************
    * Reading CSV File *
    ********************
    '''
)
import pandas as pd
df=pd.read_csv("sample.csv")
print(df.to_string())
print("\n")
print("Returning First and Last 5 rows....")
print(df)
print("\n")
print("Returning System Maximum rows")
print(pd.options.display.max_rows)
