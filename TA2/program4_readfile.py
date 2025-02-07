# Programmed by : Julius Francis De Leon
# Date Created  : 02/07/2025

# Write a python program that...
# Opens a file named "students.txt" in read mode.
# Reads the contents of the file.
# Displays the student information to the user.

print('Reading a file...')
print('===============================================')
print("       READING FILE NAMED: students.txt        ")
print('===============================================')

#Open a file named "students.txt" in read mode
file = open("students.txt", "r")

#Read the contents of the file
contents = file.read()

#Display the student information to the user
print(contents)

#Close the file
file.close()

print('===============================================')
print('File has been closed.')
print("Thank you for using the program!")
print()
