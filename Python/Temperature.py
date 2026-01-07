unit=input("Is this temperature in Celcius or Fahrenheit(C/F):")
temp=float(input("Enter the temperature:"))
if unit=="C":
    temp=temp*(9/5)+32
    print(f"The temperature in F is:{temp}")
elif unit=="F":
    temp=(temp-32)*5/9
    print(f"The temperature in C is:{temp}")
else:
    print(f"{unit} is an invalid unit of measurement")