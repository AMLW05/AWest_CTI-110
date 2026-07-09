# ==============================================================
# Name:        Angela Westmoreland
# Assignment:  P3HW1 - Grade Calculator
# Description: This program takes six numeric module grades from
#              the user, determines the lowest grade, highest
#              grade, sum, and average, and then displays the
#              letter grade based on the average.
# ==============================================================

# Enter grades for six modules (convert each entry to a float)
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add the grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for the grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display the results
print()
print('-----------Results------------')
print('Lowest Grade:', low)
print('Highest Grade:', high)
print('Sum of Grades:', total)
print('Average:', format(avg, '.2f'))
print('------------------------------')

# Determine the letter grade for the average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')