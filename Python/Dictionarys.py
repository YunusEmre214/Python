capitals={"USA":"Washington D.C.",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}
#print(dir(capitals))
#print(help(capitals))
print(capitals.get("USA"))

if capitals.get("Japan"):
    print(print("That capital exists"))
else:
    print("That capital doesn't exist")

capitals.update({"Germany":"Berlin"})
capitals.pop("China")
capitals.popitem()
#capitals.clear()
keys=capitals.keys()
print(keys)
print(capitals)

for key in capitals.keys():
    print(key)

values=capitals.values()
print(values)

for value in capitals.values():
    print(value)

items=capitals.items()
print(items)

for item in capitals.items():
    print(item)

for key,value in capitals.items():
    print(f"{key}: {value}")