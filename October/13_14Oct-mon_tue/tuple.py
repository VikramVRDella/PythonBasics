print(
    '''
    *******************
    * Tuple in Python *
    *******************
    '''
)

tuple1=("apple","banana","cherry")
print(tuple1)

tuple2=("apple",)
print(tuple2)
print(type(tuple2))

tuple3=("apple",30,"cat",40,"dog","dog")
print(tuple3)
print(type(tuple3))

print("Accessing Elements from 1st tuple")
print(tuple1[1]) # Positive Indexing
print(tuple1[-2]) # Negative Indexing
print(tuple1[1:2]) # Range of Numbers
print(tuple1[:1]) # slicing methods


print("Accessing Elements from 3rd tuple")
print(tuple3[-3:-1]) #Negative Slicing

print(
    '''
    ***************************
    * Wanna find the Elements *
    ***************************
    '''
)

ele=input("Enter the Element do you want to find : ")
if ele in tuple3:
    print(f"Yes {ele} is present in the 3rd tuple")


