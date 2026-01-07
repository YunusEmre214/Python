import math

radius=float(input("Enter the radius of a circle:"))
circumference=2*math.pi*radius
area=math.pi*(radius**2)
print(f"The circumfrence is:{round(circumference,2)}")
print(f"The area is:{round(area,2)}")
print()


a=float(input("Enter side A:"))
b=float(input("Enter side B:"))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The hipo is:{c}")

a=9
print(math.pi)
print(math.e)
res=math.sqrt(a)
res2=math.ceil(a)
print(res)
print(res2)

friends=0
friends+=1
friends*=3
friends**=2
friends=friends/2
remainder=friends%2

print()
print(friends)
print(remainder)

x=3.14
y=4
z=5

result=round(x)
result2=abs(y)
result3=pow(x,z)
result4=max(x,y,z)
result5=min(x,y,z)

print()
print(result)
print(result2)
print(result3)
print(result4)
print(result5)