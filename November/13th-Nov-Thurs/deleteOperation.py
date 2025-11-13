print(
    '''
    *********************
    * Delete Operations *
    *********************
    '''
)
import os
# file=input("Enter the file :")

while True:
    print(
        '''
        ******************************
        * Choices                    *
        * 1.Delete File              *
        * 2.Delete Folder            *         
        * 3.Delete Folder with files *
        * 4.Exit                     *
        ******************************
        '''
    )
    choice=int(input("Enter your Choice : "))
    try:
        match choice:
            case 1:
                file=input("Enter the file : ")
                if os.path.exists(file):
                    os.remove(file)
                    print("File Deleted")
                else:
                    print("File not Found")
            case 2:
                print("Caution : Removes only empty folder")
                folder=input("Enter the folder : ")
                os.rmdir(folder)
                print("Folder Deleted..")
            case 3:
                print("Works only in Linux Systems...")
                fold=input("Enter the Folder : ")
                os.system(f'rm -rf {fold}')
                print("Folder Deleted...")
            case 4:
                print("Exiting the Program....")
                break
    except:
        print("Error Occured")
