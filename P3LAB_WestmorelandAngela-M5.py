# Angela Westmoreland
# 2026
# P3LAB
# Description: Prompts the user for a dollar amount (float) and
#              displays the fewest number of dollars, quarters,
#              dimes, nickels, and pennies needed to make it.
             
# Get the amount of money from the user as a float
amount = float(input("Enter the amount of money as a float: $"))

# Convert to an integer number of cents to avoid float rounding issues
cents = int(round(amount * 100))

# Calculate how many of each unit is needed (most efficient)
dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

# If no money at all is needed, report "No change"
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
else:
    # Only print a line for a unit if at least one is needed,
    # using the singular name for 1 and the plural name otherwise
    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(dollars, "Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(quarters, "Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(dimes, "Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(nickels, "Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(pennies, "Pennies")