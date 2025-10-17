import os

print(
    '''
    ************************
    * Directory Operations *
    ************************
    '''
)

print(
    '''
    Choices:
    1.Create Directory
    2.Delete Directory
    '''
)
choice=int(input("Enter your Choice : "))

if choice==1:
    name1=input("Enter the directory name to create : ")
    os.mkdir(name1)
    print("Directory Created")
elif choice==2:
    name2=input("Enter the directory name to delete :")
    os.rmdir(name2)
    print("Directory Deleted")
else:
    print("Choose the right option")
    exit()
