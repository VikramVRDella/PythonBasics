print(
    '''
    *************************
    * Removing the txt file *
    *************************
    '''
)
import os
f=open("sample.txt", "x")
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File Removed...")
else:
    print("The File does not Exists...")
