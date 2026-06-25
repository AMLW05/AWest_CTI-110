# Angela Westmoreland
# Date
# P2HW1
# This program calculates and displays travel expenses with formatted output

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining = budget - total_expenses

print()
print("------------Travel Expenses------------")
print(f"{'Location:':<16} {destination}")
print(f"{'Initial Budget:':<16} ${budget:.2f}")
print(f"{'Fuel:':<16} ${gas:.2f}")
print(f"{'Accomodation:':<16} ${accommodation:.2f}")
print(f"{'Food:':<16} ${food:.2f}")
print("---------------------------------------")
print()
print(f"{'Remaining Balance:':<20} ${remaining:.2f}")