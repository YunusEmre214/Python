num1=float(input("Enter your first num:"))
num2=float(input("Enter your second num:"))
operator=input("Enter an operator(/,*,-,+):")

if operator=="+":
    print(f"Answer is:{num1+num2}")
elif operator=="-":
    print(f"Answer is:{num1-num2}")
elif operator=="*":
    print(f"Answer is:{num1*num2}")
elif operator=="/":
    if num2==0:
        print(f"Num2 is 0 division is cannot be happen")
    else:
      print(f"Answer is:{num1/num2}")  
else:
    print("You choosed wrong operation,please choose again.")
