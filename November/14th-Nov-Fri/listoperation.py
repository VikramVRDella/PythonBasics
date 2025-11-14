print(
    '''
    *****************
    * List Creation *
    *****************
    '''
)

lists=[]
n=int(input("Enter How many Elements :"))

for i in range(1,n+1):
    ele=int(input(f"Enter the element {i} :"))
    lists.append(ele)

print(lists)
