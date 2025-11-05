print(
    '''
    ***********************
    *    File Handling    *
    ***********************
    '''
)
print("Opening a Text File...")
f=open("demo.txt")
print(f.read())
print("\n")
print("Reading Specific part of the file.......")
d=open("demo.txt")
print(d.read(2))
print("Returning One line from the file.....")
s=open("demo.txt")
print(s.readline())
