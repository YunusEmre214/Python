name=input("Enter your full name:")
phone=input("Enter your phone number:")
result=len(name)
print(result)

result2=name.find(" ")
print(result2)

result3=name.rfind("o")
print(result3)

result4=name.capitalize()
print(result4)

result5=name.upper()
print(result5)

result6=name.lower()
print(result6)

result7=name.isdigit()
print(result7)

result8=name.isalpha()
print(result8)

result9=phone.count("-")
print(result9)

result10=phone.replace("-"," ")
print(result10)

usarname=input("Enter a username:")
usarname.find(" ")
usarname.isalpha()
if len(usarname)>12:
    print("Your username can't be more than 12 charcaters")
elif not usarname.find(" ")==-1:
    print("Your username can't contain spaces")
elif not usarname.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welecome {usarname}")