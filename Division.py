# This is the division algorithm

dividend = int(input(print("type the dividend")))
divisor = int(input(print("type the divisor")))
remainder = dividend
quotient = 0

while remainder >= divisor:
    remainder = remainder - divisor
    quotient = quotient + 1

print("Remainder: " + str(remainder) + " Quotient: " + str(quotient))
