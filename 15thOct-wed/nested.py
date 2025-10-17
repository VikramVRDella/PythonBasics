print(
    '''
    *********************
    * Nested Dictionary *
    *********************
    '''
)

dict1={
    "child1":
    {
        "name":"John",
        "age" : 32,
        "city":"NewDelhi"
    },
    "child2":
        {
            "name":"Judy",
            "age" : 28,
            "city":"America"
        },
    "child3":
        {
            "name":"Stella",
            "age" : 32,
            "city":"Africa"
        },
    
}

print(dict1)

print("Combining Various Dictionaries")

child1={
        "name":"Dennis",
        "year": 2001,
        "city":"NewDelhi"
}
child2={
        "name":"Mary",
        "year":2004,
        "city":"America"
}
child3={
        "name":"George",
        "year":2003,
        "city":"Africa"
}

dict2={
    "child1" :child1,
    "child2" :child2,
    "child3" :child3
 }
print(dict2)

print("Accessing The Nested Dictionary....")
print(dict2["child2"] ["name"])

print("Accessing Elements using Loops......")
for x,obj in dict2.items():
    print(x)
    for y in obj:
        print(y ,":",obj[y])
