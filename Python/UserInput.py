#input()
name=input("What is your name?:")
age=input("How old are you?:")

age=int(age)
age=age+1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")

#Area Calculation
print()
length=float(input("Enter the length:"))
width=float(input("Enter the width:"))
area=length*width
print(f"Our area is {area}")


#Shopping Cart
print()
item=input("What item would you like to buy?:")
price=float(input("What is the price?:"))
quantity=int(input("How many would you like?:"))
total=price*quantity
print(total)
