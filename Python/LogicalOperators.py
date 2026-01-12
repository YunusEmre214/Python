temp=25
is_raining=False

if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


is_sunny=True
if temp>=28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temp<=0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny")
elif temp<28 and temp>0 and is_sunny:
    print("It is Warm outside")
    print("It is Sunny")
elif temp>=28 and not is_sunny:
    print("It is Hot outside")
    print("It is Cloudy")
elif temp<=0 and not is_sunny:
    print("It is Cold outside")
    print("It is Cloudy")
elif temp<28 and not temp>0 and not is_sunny:
    print("It is Warm outside")
    print("It is Cloudy")