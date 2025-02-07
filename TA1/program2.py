# A program that will count the sum of the digits 
# from a given input string.
# (use for loop and some operators under module 1 and 2)

# This will ask the user to input a string
input_string = input("Enter a string: ")

digit_sum = 0

# This block of code will count the number of each character
for char in input_string:
    if '0' <= char <= '9':  # Check if character is a digit
        digit_sum = digit_sum + int(char)  # Convert character to integer and add to sum

# Finally, this will print the result
print("===============================================")
print("      DIGIT SUM CALCULATOR by Julius De Leon   ")
print("===============================================")
print("Input String      :", "'" + input_string + "'")
print("Sum of Digits     :", digit_sum)
print("===============================================")
print("Thank you for using the program!")
