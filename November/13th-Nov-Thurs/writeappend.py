print(
    '''
    ************************
    * Write or Append File *
    ************************
    '''
)


while True:
    print(
        '''
        ***********************
        * Choices             *
        * 1.Append the File   *
        * 2.Create a New File *
        * 3.Write on the File *
        * 4.Exit              *
        ***********************
        '''
    )
    choice=int(input("Enter your Choice : "))

    try:
        if choice==1:
            file=input("Enter the File : ")
            while True:
                app=input("Enter the Words to append :")
                if app=='':
                    break
                with open(file,"a") as f:
                    f.write(app+"\n")
                    print("Appended...")
                with open(file, 'r') as f:
                    f.read()
        elif choice==2:
            filename=input("Enter the File Name : ")
            f=open(filename,"x")
            print("File Created....")
        elif choice==3:
            file=input("Enter the File : ")
            while True:
                con=input("Enter the Content : ")   
                if con=='':
                    break
                with open(file, "w") as f:
                    f.write(con)
                    print("File Written...")
                with open(file, 'r') as f:
                    f.read()
        elif choice==4:
            print("Exiting the Program...")
            break
    except:
        print("Error Occured...")
