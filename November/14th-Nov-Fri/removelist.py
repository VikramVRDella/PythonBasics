print(
    '''
    *********************
    * Remove List Items *
    *********************
    '''
)

fruits=['apple','banana','cherry','dates']
try:
    while True:
        print(
            '''
            **************************
            * Choices                *
            * 1.Remove Element       *
            * 2.Remove by Index      *
            * 3.Delete Entire List   *
            * 4.Clear the List       *
            * 5.Exit                 *
            **************************
            '''
        )
        choice=int(input("Enter your Choice : "))
        if choice ==5:
            break
        elif choice ==1:
            print(fruits)
            n=int(input("How many elements do you want to remove : "))
            for i in range(1,n+1):
                rm=input("Enter the Element want to remove : ")
                fruits.remove(rm)
                print("Element Removed...")
            print(fruits)
        elif choice ==2:
            print(fruits)
            n2=int(input("How many elements do you want to remove : "))
            for i in range(1,n2+1):
                index=int(input("Enter the Index do you want to remove : "))
                fruits.pop(index)
        elif choice==3:
            print(fruits)
            del fruits
            print("List Deleted")
        elif choice==4:
            print(fruits)
            fruits.clear()
            print(fruits)
except Exception as e:
    print(f"Error Occured {e}")
    
