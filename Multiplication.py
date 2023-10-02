# This is the division algorithm

multiplied = int(input(print("type the number you want to multiply")))
multiplier = int(input(print("type the multiplier")))
result = multiplied

for i in range(multiplier - 1):
    result = result + multiplied
    i = i + 1

print("The result is: " + str(result))
