#List=[]
fruits=["apple","orange","banana","cocount"]
print(fruits[1])
print()
fruits[0]="pineapple"
fruits.append("strawberry")
fruits.remove("orange")
fruits.insert(0,"apple")
fruits.sort()
fruits.reverse()
#fruits.clear()
print(fruits.index("apple"))
print(fruits.count("apple"))

for fruit in fruits:
    print(fruit,end=" ")
print()
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("apple" in fruits)

#Set={}
fru={"apple","orange","banana","cocount","cocount"}
print(fru)
fru.add("pineapple")
fru.remove("apple")
fru.pop()
#fru.clear()
print(fru)

#Tuple=()
fr=("apple","orange","banana","cocount","cocount")
print(fr)
print(fr.index("apple"))
print(fr.count("cocount"))
for fruit in fr:
    print(fruit,end=" ")
print()