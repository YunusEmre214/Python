


def hello(greeting,title,first_name,last_name):
    print(f"{greeting} {title}{first_name} {last_name}")
hello("Hello",title="Mr.",first_name="Sponge",last_name="Square")


for x in range(1,11):
    print(x,end=" ")
print("\n1","2","3","4",sep="-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=1,area=123,first=456,last=7890)

print(phone_num)
