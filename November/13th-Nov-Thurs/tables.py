print(
    '''
    ************************
    * Multiplication Table *
    ************************
    '''
)

table=int(input("Enter the Table:"))

print(f"{table} Multiplication Table")
for i in range(1,11):
    print(f"{table} x {i} = {table*i}")
