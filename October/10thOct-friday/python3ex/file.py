import os
print('''
    **********************
    * File Operations    *
    **********************
''')

print(
    '''
    *********************
    * Choices           *   
    * 1.Read File       *
    * 2.Create File     *
    * 3.Write File      *
    * 4.Delete File     *
    *********************
    
    '''
)
choice=int(input("Enter the Choice : "))

match choice:
    case 1:
        name1=input("Enter the file name to read : ")
        f=open(name1)
        print("Reading...")
        print(f.read())
    case 2:
        name2=input("Enter the file name to create : ")
        f=open(name2,"x")
        print("File Created")
    case 3:
        name3=input("Enter the file name to write : ")
        f=open(name3,"w")
        content=input("Enter the content : ")
        f.write(content)
        print("Written")
        show=input("Want to show (y/n) : ")
        if show=="y":
            v=f.read(name3)
            print(v)
        else:
            exit()
    case 4:
        name4=input("Enter the file name to remove : ")
        os.remove(name4)
    case _:
        print("Choose a right choice")
        
        
