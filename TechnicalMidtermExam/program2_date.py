# ===============================================
# Programmed by : Julius Francis De Leon
# Date Created  : 02/10/2025
# ===============================================

# Create a program that will translate a given date format in
# mm/dd/yyyy to a more human-readable format like: January 1, 2023

print("===============================================")
print("          DATE TRANSLATOR (Program 2)          ")
print("===============================================")

# Ask the user to input the date in a given format (mm/dd/yyyy format)
date_input = input("Enter the date (mm/dd/yyyy): ")

# Using split to divide the date into parts using "/"
parts = date_input.split("/")

# Divide the date into month, day, and year and month and day are converted to integers
month = int(parts[0])
day = int(parts[1])
year = parts[2]

# Created a list of month names to use for translation
months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

# Get the month name from the list
month_name = months[month - 1]

# Print the interactive output
print("-----------------------------------------------")
print("Hello! You entered the date", month_name, str(day) + ",", year + ".")
print("That looks like a great day!")
print("-----------------------------------------------")
print("Thank you for using the program!")
print(" ")
