doubles=[]

for x in range(1,11):
    doubles.append(x*2)

print(doubles)

double=[x*2 for x in range(1,11)]

print(double)

triples=[y*3 for y in range(1,11)]

print(triples)


squares=[z*z for z in range(1,11)]

print(squares)

fruits=["apple","orange","banana","coconut"]
fruits=[fruit.upper() for fruit in fruits]
print(fruits)

fruits_chars=[fruit[0] for fruit in fruits]
print(fruits_chars)


numbers=[1,-2,3,-4,5,-6,8,-7]
positive_nums=[num for num in numbers if num>0]
negative_nums=[num for num in numbers if num<0]
even_nums=[num for num in numbers if num%2==0]
odd_nums=[num for num in numbers if num%2!=0]


print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades=[84,43,61,90,64,24]
passing_grades=[grade for grade in grades if grade>50]

print(passing_grades)