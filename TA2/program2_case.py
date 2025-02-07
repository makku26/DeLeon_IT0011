# Programmed by : Julius Francis De Leon
# Date Created  : 02/07/2025

# Write a python program that...
# Input the user's first name and last name
# Concatenate the input names into a full name
# Display the full name in both upper and lower case
# Count and display the length of the full name

print('===============================================')
print("       STRING MANIPULATIONS (Program 2)       ")
print('===============================================')
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print('===============================================')
print(' ')

print('===============================================')
print("         STRING MANIPULATIONS OUTPUTS       ")
print('===============================================')
print("Full Name          :", full_name)
print("Full Name (Upper)  :", full_name.upper())
print("Full Name (Lower)  :", full_name.lower())
print("Length of Full Name:", len(full_name))
print('===============================================')
print(' ')