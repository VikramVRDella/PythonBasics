print(
    '''
    ************************
    * Cleaning Empty Cells *
    ************************
    '''
)
import pandas as pd

df=pd.read_csv("data.csv")
new=df.dropna()
print(new.to_string())
print("\n")
print("Returning with Null Values.......")
# df=pd.read_csv("data.csv")
df.dropna(inplace=True)
print(df.to_string())
print("\n")
print("Filling Empty Values....")
df.fillna(130,inplace=True)
print(df.to_string())
print("\n")
print("Replace Values with Mean, Median, Mode......")
x=df['Calories'].mean()
df.fillna({'Calories': x},inplace=True)
print(df.to_string())
y=df['Duration'].median()
df.fillna({'Duration':y},inplace=True)
print(df.to_string())
print("\n")
z=df['Maxpulse'].mode()[0]
df.fillna({'Maxpulse':z},inplace=True)
print(df.to_string())
