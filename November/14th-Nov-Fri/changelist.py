print(
    '''
    ***************************
    * Change Elements in List *
    ***************************
    '''
)

def change_list():
    fruits=['apple','orange','mango','pineapple','guava']
    print(f"Default List : {fruits}")
    choice=input("Want to use default list (y/n) : ")
    if choice == 'n':
        a=[]
        n=int(input("How many Elements : "))
        cho=input("Want to use integer or string list (i/s) : ")
        for i in range(1,n+1):
            if cho=='i':
                ele=int(input(f"Enter the Elements {i} : "))
            elif cho=='s':
                ele=input(f"Enter the Elements {i} : ")

            a.append(ele)
        ch=input("Wanna change the Element (y/n): ")
        if ch =='y':
            print(f"Your List : {a}")
            index=int(input("Enter the Index want to change : "))
            if cho=='i':
                element=int(input("Enter the Element you want to change : "))
            elif cho=='s':
                element=input("Enter the Element you want to change : ")
            a[index]=element
            print("Element Changed")
            print(a)
            print("Thank you")
        else:
            print(a)
            print("Thank you")

    else:
        indexs=int(input("Enter the Index want to change : "))
        elements=input("Enter the Element you want to change : ")
        fruits[indexs]=elements
        print("Element Changed")
        print(fruits)
        print("Thank You")       

change_list()
