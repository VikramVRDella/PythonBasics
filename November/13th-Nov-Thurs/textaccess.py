print(
    '''
    ********************
    * Read Text Files  *
    ********************
    '''
)

file=input("Enter the File to read: ")

while True:
    print(
        '''
        ********************
        * Choices          *
        * 1.Whole File     *
        * 2.Read by Line   *
        * 3.Exit           *
        ********************
        '''
    )
    
    choice=int(input("Enter your Choice : "))

    f=open(file)
    if choice== 1:
        with open(file) as f:
            print(f.read())
    elif choice==2:
        lines=int(input("Enter how many lines you want to read : "))
        for file in range(lines):
            line=f.readline()
            print(line)
            if not line:
                print("End of the File..")
                break
    elif choice==3:
        print("Exit the Program")
        break
    else:
        print("Enter vaild Choice...")

