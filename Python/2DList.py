fruits=["apple","orange","banana","cocount"]
vegetables=["celerey","carrots","potatoes"]
meats=["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats]
#groceries=[["apple","orange","banana","cocount"],
#           ["celerey","carrots","potatoes"],
#           ["chicken","fish","turkey"]]

print(fruits)
print(groceries)
print(groceries[1][0])

for collection in groceries:
    print(collection)
print()
for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()
num_pad=((1,2,3),(4,5,6),(7,8,9),("'",0,"$"))
for row in num_pad:
    print(row)
print()
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()