print(
    '''
    ******************
    * Sum of Numbers *
    ******************
    '''
)

num=[]
sums=0

for i in range(5):
    number=int(input(f"Enter the Number {i+1} :"))
    num.append(number)

for i in range(5):
    sums+=num[i]

print(sums)
