import random

low=1
high=100
options=("rock","paper","scissors")
cards=["2","3","4","5","6","7","8","9"]

num=random.randint(low,high)
number=random.random()
option=random.choice(options)
random.shuffle(cards)

print(num)
print(number)
print(option)
print(cards)