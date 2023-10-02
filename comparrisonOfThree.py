x = int(input("Type a value"))
y = int(input("Type a value"))
z = int(input("Type in a value"))

if x >= y and x >= z:
    print("The greatest number is: " + str(x))

elif y >= x and y >= z:
    print("The greatest number is: " + str(y))

elif z >= x and z >= y:
    print("The greatest number is: " + str(z))

