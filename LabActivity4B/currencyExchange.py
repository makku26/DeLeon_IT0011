# ===================================================================
#   PYTHON PROGRAMMING (Laboratory Activity 4B: Set and Dictionary)
#               Submitted by: JULIUS FRANCIS DE LEON
#                      Date: March 04, 2025
# ===================================================================

# Code starts HERE!!!
import csv

# Define the filename for the currency exchange rates
filename = "currency.csv"

# Print the program header
print("╔══════════════════════════════════════════════════╗")
print("║       >>> CURRENCY EXCHANGE CALCULATOR <<<       ║")
print("║            by Julius Francis De Leon             ║")
print("╚══════════════════════════════════════════════════╝")

# Load currency exchange rates from the CSV file
exchange_rates = {}
try:
    with open(filename, mode='r', encoding='latin-1') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 3:  # Ensure the row has exactly 3 columns
                code, name, rate = row
                exchange_rates[code.strip().upper()] = {
                    "name": name.strip(),
                    "rate": float(rate),
                }
            else:
                print(f"Warning: Skipping invalid row: {row}")
except FileNotFoundError:
    print(f" Error: The file '{filename}' was not found.")
    exit()
except Exception as e:
    print(f" An error occurred while reading the file: {e}")
    exit()

# Get user input for the amount and target currency
try:
    amount = float(input(" How much dollar do you have? "))
    currency = input(" What currency you want to have? ").strip().upper()

    # Perform the conversion
    if currency in exchange_rates:
        converted_amount = amount * exchange_rates[currency]["rate"]
        currency_name = exchange_rates[currency]["name"]  # Retrieve currency name
        print(f" Your current Dollar: {amount} USD")
        print(f" Converted into {currency_name} \n With an exchange rate of {currency} {converted_amount:.2f}")
        print("════════════════════════════════════════════════════")
    else:
        print(f"\nError: Currency '{currency}' is not supported.")
except ValueError:
    print("Error: Please enter a valid number for the dollar amount.")

input(" Press ENTER to continue...")
