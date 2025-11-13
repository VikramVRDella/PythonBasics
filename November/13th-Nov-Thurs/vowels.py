print(
    '''
    ******************
    * Vowels Counter *
    ******************
    '''
)

word=input("Enter the Word : ")
count=0
vowels='aeiou'

for char in word:
    if char in vowels:
        count+=1

print(f"Number of Vowels in Given Text is {count}")
