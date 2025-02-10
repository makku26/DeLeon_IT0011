# Programmed by : Julius Francis De Leon
# Date Created  : 02/10/2025

# Create a program that will open the file numbers.txt
# and check each line if the sum of the given string
# digit numbers is palindrome.

# If the given numbers are 10,20,30,17 then you have 
# to add the numbers (77) then the number is said to be sum palindrome.

print('=====================================================')
print("            PALINDROME CHECKER (Program 1)       ")
print('=====================================================')

# Open and read the file
with open("numbers.txt", "r") as file:
    line_number = 1  
    
    # this will read the file line by line
    for line in file:
        line = line.strip()  # cleans up spaces
        numbers = line.split(",")  # splits the line using comma
        
        # this will convert valid numbers to integers
        valid_numbers = []
        for num in numbers:
            num = num.strip()
            if num != "":  # just ignores the empty values
                valid_numbers.append(int(num))
        
        # this will compute the sum of numbers
        total_sum = sum(valid_numbers)
        
        # this will check if the sum is a palindrome or not
        if str(total_sum) == str(total_sum)[::-1]:
            print(f"Line {line_number}: [{line}] Sum: {total_sum} ---> PALINDROME") # palindrome
        else:
            print(f"Line {line_number}: [{line}] Sum: {total_sum} ---> NOT a palindrome") # not a palindrome
        
        line_number += 1  # increments to the next line number
