# Activity 05 - Function

# This func performs division, ensuring no division by zero
def divide(a, b):
    if b == 0:
        print('Error! Denominator must not be equal to zero! ')
        print('Please Try Again. ')
        return None
    return a / b

def exponentiate(a, b):
    return a ** b # This line raises 'a' to the power of 'b'

# This func computes remainder, ensuring no division by zero
def remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

# This func computes the sum of numbers from 'a' to 'b' and displays the sequence
def summation(a, b):
    if a > b:
        print("Error: The second number must be greater than the first number.")
        return None
    sequence = list(range(a, b + 1))
    print(" + ".join(map(str, sequence)), "=", sum(sequence))
    return sum(sequence)

def pause():
    input("\nPress Enter to Continue...")

def main():
    while True:
        print("╔════════════════════════════════════════════╗")
        print("║   Simple Mathematical Operations Program   ║")
        print("║          by JULIUS FRANCIS DE LEON         ║")
        print("╠════════════════════════════════════════════╣")
        print("║ [D] - Division                             ║")
        print("║ [E] - Exponentiation                       ║")
        print("║ [R] - Remainder                            ║")
        print("║ [F] - Summation                            ║")
        print("║ ------------------------------------------ ║")
        print("║ [Q] - Quit the program                     ║")
        print("╚════════════════════════════════════════════╝")
        choice = input('Enter your choice: ').strip().upper()
        
        if choice == 'Q':
            print("Exiting the program. Thank you for using the Program!")
            print("Goodbyeee! :>")
            break
        
        if choice in ['I', 'D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                
                if choice == 'I':
                    result = integer_division(num1, num2)
                elif choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiate(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)
                
                if result is not None:
                    print("Result:", result)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please enter I, D, E, R, F, or Q.")
        
        pause()
        
if __name__ == "__main__":
    main()