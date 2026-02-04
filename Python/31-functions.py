def happy_birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Victor",25)
happy_birthday("Seluna",25)
happy_birthday("Azathoth",24)
happy_birthday("Yalin",26)
happy_birthday("Elena",24)
happy_birthday("Amanises",23)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due:{due_date}")

display_invoice("Victor",42.50,"04/02/2026")

def add(x,y):
    z=x+y
    return z
def subtract(x,y):
    z=x-y
    return z
def multiply(x,y):
    z=x*y
    return z
def divide(x,y):
    z=x/y
    return z

add(1,2)
print(add(3,5))
print(subtract(7,9))
print(multiply(8,7))
print(divide(3,7))


def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last
full_name=create_name("Ageon","Raikan")
print(full_name)

