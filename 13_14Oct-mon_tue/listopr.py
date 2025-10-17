print(
    '''
    ********************
    * List Operations  *
    ********************
    '''
)

list1=["apple","banana","cherry"]
print(
        '''
        ******************
        * 1.Append       *
        * 2.Insert       *
        * 3.Extend       *
        * 4.Exit         *
        ******************
        '''
    )
try:
    choice=int(input("Enter the Choice : "))
except ValueError:
    print("Please Enter the Valid Number")
match choice:
        case 1:
            print("You Chose Append Operation")
            ele1=input("Enter the Element to append : ")
            print("Element Appended")
            list1.append(ele1)
            print(list1)
        case 2:
            print("You Chose Insert Operation")
            place=int(input("Enter the Element place to be placed : "))
            ele2=input("Enter the Element to be placed : ")
            print("Element Placed")
            list1.insert(place,ele2)
            print(list1)
        case 3:
            print("You Chose Extend Operation")
            ele3=input("Enter the Elements want to extend : ")
            print("Elements Extended")
            list1.extend(ele3)
            print(list1)
        case 4:
            print("Exiting Program....Goodbye")
        case _:
            print("Enter the Correct Option")

    
liss=["apple",["ball","cat"],"dog"]
print(liss)
