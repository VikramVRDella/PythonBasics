print(
    '''
    ********************
    * Indexing of List *
    ********************
    '''
)

fruits = []
try: 
    while True:
        ele = input("Enter the Fruits Name (press Enter to stop): ")
        if ele == '':
            break
        fruits.append(ele)
    print("Fruits List:", fruits)
except Exception as e:
    print("Error Occurred on Appending a List:", e)


def Accessing(choice):
    
    if choice == 1:
        try:
            index = int(input("Enter the Index: "))
            print(f"Accessed Element is: {fruits[index]}")
        except IndexError:
            print("Index out of range!")
    elif choice == 2:
        try:
            start = int(input("Enter the Start range: "))
            stop = int(input("Enter the Stop range: "))
            print(f"Elements are: {fruits[start:stop]}")
        except IndexError:
            print("Range out of bounds!")
    elif choice == 3:
        print("Exiting Program")
    else:
        print("Invalid Choice!")


try:
    print(
            '''
            *******************************
            * Choices for Access          *
            * 1. Index                    *
            * 2. Range of Index           *
            * 3. Exit                     *
            *******************************
            '''
        )
    choice = int(input("Enter your Choice: "))
    Accessing(choice)
except ValueError:
    print("Please enter a valid number for choice.")
