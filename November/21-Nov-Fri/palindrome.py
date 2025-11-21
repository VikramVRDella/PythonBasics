def palindrome(word):
    reverse=word[::-1]
    if word==reverse:
        return ("Given String is Palindrome")
    else:
        return ("Given String is not Palindrome")

while True:
    choice=input("Enter a Word (or enter exit to leave): ")
    if choice == 'exit':
        break
    result=palindrome(choice)
    print(result)
    