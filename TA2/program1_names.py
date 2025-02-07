# Programmed by : Julius Francis De Leon
# Date Created  : 02/07/2025

# Write a python program that...
# Concatenate your first name and last name into a full name
# Slice the full name to extract first three characters of the first name
# Use string formatting to create a greating message that includes the sliced first name

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name

age = int(input("Enter your age: "))

#slice the first three characters of the first name using string manipulation
sliced_name = first_name[:3]

print('===============================================')
print("       STRING MANIPULATIONS (Program 1)       ")
print('===============================================')
print("Full Name          :", full_name)
print("Sliced Name        :", sliced_name)
# used the FORMAT() function
print("Greeting Message   : Greetings, {}! You are {} years old.".format(sliced_name, age))
print('===============================================')
