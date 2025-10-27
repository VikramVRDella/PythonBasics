def duplicate(x):
    return list(dict.fromkeys(x))

my_list=['a','b','c','d','e','a','b','c','d']

print(f"Given List : {my_list}")
print(f"Duplicate Removed disk : {duplicate(my_list)}")