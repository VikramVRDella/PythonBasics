print(
    '''
    ***********************
    *  Loop Dictionaries  *
    ***********************
    '''
)

dict1={
    "name":"John",
    "age":32
}

print("Printing Keys from the Dictionary")
for x in dict1.keys():
    print(x)

print("Printing Values from the Dictionary")
for x in dict1.values():
    print(x)

print("Printing Both Keys and Values")
for x,y in dict1.items():
    print(x,y)
