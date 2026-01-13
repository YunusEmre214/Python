for x in range(3):
    for y in range(1,10):
        print(y,end=" ")
    print()

#for x in range(1,10):
#    print(x,end=" ")

rows=int(input("Enter the number of rows:"))
colm=int(input("Enter the number of colm:"))
symbol=input("Enter a symbol to use:")
for x in range(rows):
    for y in range(colm):
        print(symbol,end=" ")
    print()