print(
    '''
    *************************
    *   Copy Dictionaries   *
    *************************
    '''
)

dict1={
    "name":"Doe",
    "age":32,
    "city":"NewYork"
}

dict2=dict1.copy()
print("Original : ",dict1)
#Copied Dictionary
print("Copied : ",dict2)

print("Dictionary copied using \"dict\" Function")
mydict=dict(dict1)
print(mydict)

