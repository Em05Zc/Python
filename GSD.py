# This is the GSD algorithm by Euclides (Greatest Common Divisor)

x = int(input(print("type in a positive integer which can be divided by two\n")))
y: int = int(input(print("type in a different positive integer which can be divided by two\n")))


def gsd(a, b):
    c = 0
    if a > 0 and b > 0:
        pass
    else:
        if a <= 0 and b <= 0:
            print("You did not follow the instructions both numbers are negative or 0")
            exit(404)

        elif a <= 0:
            print("You did not follow the instructions the first number is negative or 0")
            exit(404)

        else:
            print("You did not follow the instructions the second number is negative or 0")
            exit(404)

    if a % 2 == 0 and b % 2 == 0:
        pass
    else:
        if a % 2 != 0 and b % 2 != 0:
            print("You did not follow the instructions both numbers cannot be divided by 2")
            exit(505)

        elif a % 2 != 0:
            print("You did not follow the instructions the first number cannot be divided by 2")
            exit(505)

        else:
            print("You did not follow the instructions the second number cannot be divided by 2")
            exit(505)

    while a > b or a < b:
        if a > b:
            a = a - b
            c = a
        else:
            b = b - a
            c = b

    print("The greatest common denominator is: " + str(c))


gsd(x, y)
