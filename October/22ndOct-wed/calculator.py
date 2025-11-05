print(
    '''
    *****************
    *  Calculator   *
    *****************
    '''
)
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return float(self.num1)/float(self.num2)

a=int(input("Enter the 1st Number : "))
b=int(input("Enter the 2nd Number : "))
calc=Calculator(a,b)
print(
    '''
    *********************
    * 1.Add             *
    * 2.Subract         *
    * 3.Multiply        *
    * 4.Divide          *
    *********************
    '''
)
choice = int(input("Enter your Choice : "))
match choice:
    case 1:
        print(calc.add())
    case 2:
        print(calc.sub())
    case 3:
        print(calc.mul())
    case 4:
        print(calc.div())
    case _:
        print("Choose the Correct Option")        
