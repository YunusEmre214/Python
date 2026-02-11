from car import Car

car1=Car("Mustang","2024","Red",False)
car2=Car("Corvette",2025,"blue",True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.stop()
car2.drive()
car1.describe()
car2.describe()
