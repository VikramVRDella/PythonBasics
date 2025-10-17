print(
    '''
    ********************
    *   Loop Tuples    *
    ********************
    '''
)

tuple1=("apple","ball","cherry")
for x in tuple1:
    print(x)

print("Loop tuples with the Index Numbers....")
for i in range(len(tuple1)):
    print(tuple1[i])

print("Using While Loops....")
i=0
while i<len(tuple1):
    print(tuple1[i])
    i=i+1

