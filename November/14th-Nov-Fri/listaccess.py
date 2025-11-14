print(
    '''
    ***************************
    * Accessing List Elements *
    ***************************
    '''
)

def accessing_list(lists,start,stop):
    lists=[]
    n=int(input("Enter how many elements : "))

    for  i in range(1,n+1):
        ele=int(input(f"Enter the Element {i} : "))
        lists.append(ele)
    print(f"Entire List : {lists}")
    return (f"You Accessed : {lists[start:stop]}")

st=int(input("Enter the Starting Index : "))
so=int(input("Enter the Stoping Index : "))
a=[]
print(accessing_list(a,st,so))
