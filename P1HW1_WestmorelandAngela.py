# Angela Westmoreland
# Date
# P1HW1
# This program calculates exponents and performs addition and subtraction

print("-----Calculating Exponents-----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()

result = base ** exponent
print(str(base) + " raised to the power of " + str(exponent) + " is " + str(result) + " !!")
print()

print("-----Addition and Subtraction-----")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
print()

total = num1 + num2 - num3
print(str(num1) + " + " + str(num2) + " - " + str(num3) + " is equal to " + str(total))