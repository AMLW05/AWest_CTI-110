# Angela Westmoreland
# 2026
# P2HW2
# This program stores module grades in a list and displays grade statistics

# Pseudocode:
# 1. Ask user to enter a grade for each of the 6 modules
# 2. Store all grades in a list
# 3. Use min() to find the lowest grade
# 4. Use max() to find the highest grade
# 5. Use sum() to add all grades together
# 6. Calculate average by dividing sum by number of grades
# 7. Display all results formatted in a neat column

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / 6

print()
print("------------Results------------")
print(f"{'Lowest Grade:':<16} {lowest}")
print(f"{'Highest Grade:':<16} {highest}")
print(f"{'Sum of Grades:':<16} {total}")
print(f"{'Average:':<16} {average:.2f}")
print("---------------------------------------")