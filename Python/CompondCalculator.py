principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the principle amount:"))
    if principle<=0:
        principle("Principle can't be less than or equal the zero.")
    else:
        break
while True:
    rate=float(input("Enter the interest rate:"))
    if rate<=0:
        rate("Interest rate can't be less than or equal the zero.")
    else:
        break
while True:
    time=float(input("Enter the time in years:"))
    if time<=0:
        time("Time can't be less than or equal the zero.")
    else:
        break
total=principle*(1+rate/100)**time
print(f"Balance after {time} years is:{total:.2f}")
