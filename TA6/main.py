# Activity 06 - OOP and Exception
# Date created: March 29, 2025
# Submitted by JULIUS FRANCIS DE LEON from TW24

import csv
import os

FILE_NAME = 'items.csv' # File name where items will be stored

class Item:
    def __init__(self, item_id, name, description, price):
        self.validate_inputs(item_id, name, description, price) # check if the inputs are valid
        self.id = item_id # unique ID
        self.name = name # item name
        self.description = description # item descriptionn
        self.price = float(price)  # Convert to float for proper handling
        
    @staticmethod
    def validate_inputs(item_id, name, description, price):
        if not item_id.strip():
            raise ValueError("Item ID cannot be empty.")
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if not description.strip():
            raise ValueError("Description cannot be empty.")
        try:
            if float(price) <= 0:
                raise ValueError("Price must be a positive number.")
        except ValueError:
            raise ValueError("Price must be a valid number.")

    def to_list(self):
        return [self.id, self.name, self.description, str(self.price)]
        
class ItemManager:
    def __init__(self):
        self.items = self.load_items()
        
    def load_items(self):
        items = {}
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        try:
                            items[row[0]] = Item(*row)
                        except ValueError:
                            print(f"Skipping invalid item entry: {row}")
        return items
    
    def save_items(self):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            for item in self.items.values():
                writer.writerow(item.to_list())
                
    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            raise ValueError("Item ID already exists.")
        self.items[item_id] = Item(item_id, name, description, price)
        self.save_items()
        print('\n╔═════════════════════════════════════╗')
        print("║       Item Added Successfully!      ║")
        print("╚═════════════════════════════════════╝")
        input("\nPress ENTER to continue...")
        
    def read_items(self):
        if not self.items:
            print("No Items Available...        ")
        else:
            print("╔══════╤══════════════════════╤═════════════════════════════════════════╤═══════════╗")
            print("║  ID  │ Name                 │ Description                             │ Price     ║")
            print("╠══════╪══════════════════════╪═════════════════════════════════════════╪═══════════╣")
            for item in self.items.values():
                print(f"║ {item.id:<4} │ {item.name:<20} │ {item.description:<39} │ ₱{float(item.price):>8} ║")
            print("╚══════╧══════════════════════╧═════════════════════════════════════════╧═══════════╝")
        input("\nPress ENTER to continue...")

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            raise ValueError("Item ID not found.")
        
        item = self.items[item_id]

        if name:
            item.name = name
        if description:
            item.description = description
        if price:
            try:
                if float(price) <= 0:
                    raise ValueError("Price must be a positive number.")
                item.price = float(price)
            except ValueError:
                raise ValueError("Price must be a valid number.")

        self.save_items()
        print("\n╔═════════════════════════════════════╗")
        print("║       Item updated successfully!    ║")
        print("╚═════════════════════════════════════╝")
        input("\nPress ENTER to continue...")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            self.save_items()
            print("\n╔═════════════════════════════════════╗")
            print("║       Item deleted successfully!    ║")
            print("╚═════════════════════════════════════╝")
            input("\nPress ENTER to continue...")
        else:
            raise ValueError("Item ID not found.")


def display_menu():
    print("\n╔═════════════════════════════════════╗")
    print("║     ITEM MANAGEMENT SYSTEM MENU     ║")
    print("╠═════════════════════════════════════╣")
    print("║ [1] Add Item                        ║")
    print("║ [2] View Items                      ║")
    print("║ [3] Update Item                     ║")
    print("║ [4] Delete Item                     ║")
    print("║ ----------------------------------- ║")
    print("║ [5] Exit the program                ║")
    print("╚═════════════════════════════════════╝")


def main():
    manager = ItemManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                print("\n╔═════════════════════════════════════╗")
                print("║      SELECTED OPTION: ADD ITEM      ║")
                print("╚═════════════════════════════════════╝")
                item_id = input("Enter Item ID          : ")
                name = input("Enter Item Name        : ")
                description = input("Enter Item Description : ")
                price = input("Enter Item Price       : ")
                manager.create_item(item_id, name, description, price)

            elif choice == '2':
                print("\n╔═════════════════════════════════════╗")
                print("║     SELECTED OPTION: VIEW ITEM      ║")
                print("╚═════════════════════════════════════╝")
                manager.read_items()

            elif choice == '3':
                print("\n╔═════════════════════════════════════╗")
                print("║    SELECTED OPTION: UPDATE ITEM     ║")
                print("╚═════════════════════════════════════╝")
                item_id = input("Enter Item ID   : ")
                print("\n[Leave blank to keep unchanged]")
                name = input("New Name        : ") or None
                description = input("New Description : ") or None
                price = input("New Price       : ") or None
                manager.update_item(item_id, name, description, price)

            elif choice == '4':
                print("\n╔═════════════════════════════════════╗")
                print("║    SELECTED OPTION: DELETE ITEM     ║")
                print("╚═════════════════════════════════════╝")
                item_id = input("Enter Item ID to delete: ")
                manager.delete_item(item_id)

            elif choice == '5':
                print("\n╔═════════════════════════════════════╗")
                print("║  Exiting the program... Thank you!  ║")
                print("╚═════════════════════════════════════╝")
                print("\nProgrammed by JULIUS FRANCIS DE LEON")
                print("Section: TW24\n")
                input("\nPress Enter to continue...")
                break

        except ValueError as e:
            print(f"\nERROR: {e}")
        except Exception as e:
            print(f"\n⚠ Unexpected error: {e}")


if __name__ == "__main__":
    main()
