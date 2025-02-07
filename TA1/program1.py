# Create the following program
#   A program that will display the number of vowels,
#   consonants, spaces, and other characters given an input string.
#   (use for loop and some operators under module 1 and 2)

#This will ask the user to input a string
input_string = input("Enter a string: ")

#Initializing counters for each character
vowels_counter = 0
consonants_counter  = 0
spaces_counter  = 0
others_counter  = 0

# Define vowels and consonants
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

#This block of code will count the number of each character
for char in input_string:
    if char in vowels:
        vowels_counter  += 1
    elif char in consonants:
        consonants_counter  += 1
    elif char == " ":
        spaces_counter  += 1
    else:
        others_counter  += 1

#Finally, this will print the results
print("===============================================")
print("      CHARACTER COUNTER by Julius De Leon      ")
print("===============================================")
print("Input String      :", "'" + input_string + "'")
print("Vowels            :", vowels_counter )
print("Consonant         :", consonants_counter )
print("Spaces            :", spaces_counter )
print("Other Characters  :", others_counter )
print("===============================================")
print("Thank for using the program!")