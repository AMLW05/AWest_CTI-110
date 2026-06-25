# Angela Westmoreland
# Date
# P1HW2
# This program calculates and displays travel expenses

# Pseudocode:
# 1. Display program title
# 2. Ask user for their budget
# 3. Ask user for their travel destination
# 4. Ask user for gas, accommodation, and food expenses
# 5. Add all expenses together
# 6. Subtract total expenses from budget
# 7. Display a summary showing location, budget, expenses, and remaining balance

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining = budget - total_expenses

print()
print("------------Travel Expenses------------")
print("Location: " + destination)
print("Initial Budget: " + str(budget))
print()
print("Fuel: " + str(gas))
print("Accomodation: " + str(accommodation))
print("Food: " + str(food))
print()
print("Remaining Balance: " + str(remaining))