#String
first_name="Victor"
food="strawberry"
email="vic@gmail.com"


print(first_name)
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integer
age=21
quantity=3
num_of_students=17

print()
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"There are {num_of_students} students have in your class")

#Float
price=10.99
gpa=3.66
distance=5.5

print()
print(f"The price is {price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}")

#Boolean
is_student=True
for_sale=True


print()
print(f"Are you a student? {is_student}")
if is_student:
    print("You are a student")
else:
    print("You are not a student")
if for_sale:
    print("The item is for sale")
else:
    print("That item is not available")
