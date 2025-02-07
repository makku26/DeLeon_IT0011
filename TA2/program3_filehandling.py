# Programmed by : Julius Francis De Leon
# Date Created  : 02/07/2025

# Write a python program that...
# Creates a string containing the collected information in a formatted way.
# Opens a file named "students.txt" and append mode and writes the formatted information to the file.
# Displays a confirmation message indicating that the information has been saved.

print('===============================================')
print("           FILE HANDLING (Program 3)           ")
print('===============================================')

first_name = input("Enter your first name     : ")
last_name = input("Enter your last name      : ")
full_name = first_name + " " + last_name
age = int(input("Enter your age            : "))
contact_number = input("Enter your contact number : ")
course = input("Enter your course         : ")
print('===============================================')
print(' ')

#Open a file named "students.txt" in append mode
file = open("students.txt", "a")

#Write the formatted information to the file
file.write("Full Name          : " + full_name + "\n")
file.write("Age                : " + str(age) + "\n")
file.write("Contact Number     : " + contact_number + "\n")
file.write("Course             : " + course + "\n")

#display a confirmation message
print("Information has been saved successfully!")
print('File Name: students.txt')
print(' ')

#close the file
file.close()
