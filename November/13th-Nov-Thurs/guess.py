print(
    '''
    ********************
    * Guess the Number *
    ********************
    '''
)
import random

rand=random.randint(1,100)
while True:
    num=int(input("Guess the Number :"))
    rand=random.randint(1,100)
    if num==0 :
        break
    if num==rand:
        print("You Win")
        break
    else:
        print(f"Try Again The Number is {rand}")
