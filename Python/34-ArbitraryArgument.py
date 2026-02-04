def add(*args):
    print(type(args))
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("Dr.","Spongebob","Harold","Squarepants","IV")
print()
def print_address(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="MI",
              zip=54321)

print()
def shippping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shippping_label("Dr.","Spongebob","Harold","Squarepants","IV",
                street="123 Fake St.",
                #apt="100",
                pobox="PO box #1001",
                city="Detroit",
                state="MI",
                zip=54321)
