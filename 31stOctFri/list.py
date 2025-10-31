list1=[7,14,21,53,67,1,4,5]

min=list1[0]
high=list1[0]

for i in list1:
    if i< min:
        min=i
for j in list1:
    if j>high:
        high=j

print("Lowest Value :", min)
print("Highest Value :", high)
