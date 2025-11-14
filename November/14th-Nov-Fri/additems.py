print(
    '''
    *********************
    * Add items to list *
    *********************
    '''
)
print(
    '''
    ***********************
    * Choice              *
    * 1.Append List Item  *
    * 2.Extend List       *
    * 3.Insert List Item  *
    * 4.Exit              *
    ***********************
    '''
)

while True:
    choice=int(input("Choose one Option (1-4) : "))
    fruits=['apple','cherry','banana']
    if choice==4:
        break
    elif choice==1:
        print(fruits)
        n=int(input("How many Elements do you want to append : "))
        if n==1:
            ele=input("Enter the Element want to append : ")
            fruits.append(ele)
            print(fruits)
        elif n>2:
            for i in range(1,n+1):
                ele=input(f"Enter the Element {i} : ")
                fruits.append(ele)
                print(fruits)
    elif choice==2:
        a=[]
        t=int(input("How many elements on extend list : "))
        for i in range(1,t+1):
            elem=input(f"Enter the Element {i} : ")
            a.append(elem)
        fruits.extend(a)
        print("List Extended...")
        print(fruits)
        
    elif choice==3:
        index=int(input("Enter the index do you want to insert : "))
        eleme=input("Enter the Element do you want to insert : ")

        fruits.insert(index,eleme)
        print(fruits)
    else:
        print("Enter the Vaild Option.....")
        
