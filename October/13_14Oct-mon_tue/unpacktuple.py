print(
    '''
    ********************
    * Unpacking Tuples *
    ********************
    '''
)

tuple1=("apple","banana","grapes")
(green,red,yellow)=tuple1
print(green)
print(yellow)
print(red)

print("Using Astrick ")
(green,*red)=tuple1
print(green)
print(red)

print("Using Astrick ")
(*green,red)=tuple1
print(green)
print(red)
