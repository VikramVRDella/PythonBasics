print(
    '''
    **********************
    * Exception Handling *
    **********************
    '''
)

try:
    print(x)
except:
    print("An Exception Occured....")
print("\n")
print("An Additional Exception...")
try:
    print(x)
except NameError:
    print("Variable x is not defined....")
except:
    print("Something went Wrong.....")
print("\n")
print("A Else statement in try-catch Exception....")
try:
    print("Hello")
except:
    print("Something Went Wrong....")
else:
    print("Nothing Went Wrong.....")
print("\n")
print("Writing a file using try catch")
try:
    f=open("demo.txt")
    try:
        f.write("Hello, How are You")
    except:
        print("Something went Wrong...")
    finally:
        f.close()
except:
    print("Something went wrong")
