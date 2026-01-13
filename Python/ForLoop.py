credit_card="1234-4362-351-5451"

for x in reversed(range(1,11,2)):
    print(x)
print("Happy New Year!")

for x in credit_card:
    print(x)
for x in range(1,21):
    if(x==13):
        continue
    else:
        print(x)