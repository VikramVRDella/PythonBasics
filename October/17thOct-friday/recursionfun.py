print(
    '''
    **********************
    * Recursion Function *
    **********************
    '''
)
def countdown(n):
    if n<=0:
        print("Done!!!")
    else:
        print(n)
        countdown(n-1)

a=int(input("Enter the Number to start Countdown : "))
countdown(a)
print("\n")
print(
    '''
    **********************
    * Factorial Function *
    **********************
    '''
)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

b=int(input("Enter the Number for Factorial : "))
print(f"Factorial of {b} is",fact(b))
print("\n")
print(
    '''
    ********************
    * Fabonacci Series *
    ********************
    '''
)
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
c=int(input("Enter the Number for Fibonacci Series : "))
print(fibo(c))
print("\n")
print(
    '''
    ************************
    * Recursion with Lists *
    ************************
    '''
)

def listfun(n):
    if len(n)==0:
        return 0
    else:
        return n[0]+listfun(n[1:])

list1=[1,2,4,5,6]
print(list1)
print(listfun(list1))
print("\n")
print(
    '''
    *************************
    * Maximum Value in List *
    *************************
    '''
)

def maxfun(n):
    if len(n)==1:
        return n[0]
    else:
        max1=maxfun(n[1:])
        return  n[0] if n[0]>max1 else max1
list2=[3,23,4,223,1,4,5]
print(list2)
print(maxfun(list2))
print("\n")
