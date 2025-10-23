print(
    '''
    **********************
    * Create/Write Files *
    **********************
    '''
)
print("Appending to the File....")
with open("demo.txt", "a") as f:
    f.write("Hello")
with open("demo.txt", "r") as f:
    content=f.read()
print(content)
print("\n")
print("Writing to the File.....")
with open("demo.txt", "w") as f:
    f.write("Hello this is New Content...")
with open("demo.txt", "r") as f:
    content=f.read()
print(content)
print("\n")
print("Creating a New File.....")
f=open("hello.txt", "x")
with open("demo.txt", "w") as f:
    f.write("Hello this is from New File")
with open("demo.txt", "r") as f:
    content=f.read()
print(content)
print("\n")
