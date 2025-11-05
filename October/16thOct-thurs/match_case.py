print(
    '''
    **************************
    *  Match-Case Statements *
    **************************
    '''
)

#Day Finder Match case with Default Values
num=int(input("Enter the  Number : "))

match num:
    case 1:
        print("Its Monday")
    case 2:
        print("Its Tuesday")
    case 3:
        print("Its Wednesday")
    case 4:
        print("Its Thursday")
    case 5:
        print("Its Friday")
    case _:
        print("Looking Forward to the Weekend")

#Weekday and Weekend Finder combine Values

num1=int(input("Enter the Number : "))

match num1:
    case 1|2|3|4|5:
        print("It's A Weekday")
    case 6|7:
        print("It's A weekEnd")


#combining if-Else Statements

day=int(input("Enter a day (in numbers) : "))
month=10

match day:
    case 1|2|3|4|5 if month== 10 :
        print("You're in the weekday of October...")
    case 1|2|3|4|5 if month==11:
        print("You're in the weekday of  November...")
