# ===================================================================
#          PYTHON PROGRAMMING (Activity 04: List and Tuple)
#               Submitted by: JULIUS FRANCIS DE LEON
#                      Date: March 04, 2025
# ===================================================================

# Create a record management program given a list of students records
# OTHER FEATURES:
#  - Added a CONFIRMATION before saving, deleting, and editing records
#  - Uses .strip() and .upper() to clean up user inputs

# code starts HERE!!!
import os

student_records = [] # Created a list to store student records
filename = "" # just to initialize the variable

# Created Two Functions to Open and Save Records to REDUCE line of codes :>
# This function opens a file and LOADS the records to the list
def open_records(filename):
    global student_records
    try:
        with open(filename, "r") as f:
                student_records = [tuple(line.strip().split(", ")) for line in f]
        print("")
        print("════════════════════════════════════════════════════")
        print(f"A Record Has Successfully Loaded from              ")
        print(f"'{filename}' to the List!")
        print("════════════════════════════════════════════════════")
    except FileNotFoundError:
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║ Oh no! FILE NOT FOUND.                           ║")
        print("║ Please double check the filename and try again.  ║")
        print("╚══════════════════════════════════════════════════╝")
    except Exception as e:
        print(f"An error occurred: {e}")

# This function saves the records to a file
def save_records(filename):
    global student_records
    try:
        with open(filename, "w") as f:
            for record in student_records:
                f.write(", ".join(map(str, record)) + "\n") # Write records to the file
        print("")
        print("════════════════════════════════════════════════════")
        print(f"A Record Has Successfully Saved from               ")
        print(f"'{filename}'!")
        print("════════════════════════════════════════════════════")
    except Exception as e:
        print(f"An error occurred: {e}")

# MAIN Menu for the program
while True:
    print("╔══════════════════════════════════════════════════╗")
    print("║         STUDENT RECORD MANAGEMENT SYSTEM         ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ MENU OPTIONS               **select an option**  ║")
    print("║  [1] - Open File                                 ║")
    print("║  [2] - Save File                                 ║")
    print("║  [3] - Save as File                              ║")
    print("║  [4] - Show All Student Records                  ║")
    print("║  [5] - Show Student Record                       ║")
    print("║  [6] - Add Record                                ║")
    print("║  [7] - Edit Record                               ║")
    print("║  [8] - Delete Record                             ║")
    print("║  [0] - EXIT THE PROGRAM                          ║")
    print("╚══════════════════════════════════════════════════╝")
    choice = input("Enter your choice: ")
    
    # This lets the user exit the program
    if choice == "0":
        print("")
        print("\t╔══════════════════════════════════╗")
        print("\t║      * EXITING THE PROGRAM *     ║")
        print("\t╠══════════════════════════════════╣")
        print("\t║ Thank you for using the program! ║")
        print("\t║                                  ║")
        print("\t║           SUBMITTED BY:          ║")
        print("\t║      JULIUS FRANCIS DE LEON      ║")
        print("\t║               TW24               ║")
        print("\t║       Date: March 04, 2025       ║")
        print("\t╚══════════════════════════════════╝\n")
        break
    
    # This lets the user to search and open a file
    elif choice == "1":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║            CURRENT OPTION: Open File             ║")
        print("╚══════════════════════════════════════════════════╝")
        filename = input("Enter the filename: ").lower()
        open_records(filename)
        
    # This lets the user to save the records to a file
    elif choice == "2":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║            CURRENT OPTION: Save File             ║")
        print("╚══════════════════════════════════════════════════╝")
        if filename:  # Checks if filename is NOT EMPTY
            print("")
            print("Are you sure you want to SAVE this current records?")
            print("NOTE: This action CANNOT be undone. (yes/no)")
            print("")
            confirm = input("Confirm? : ").strip().lower()
            
            if confirm == "yes":
                save_records(filename) 
            else:
                print("════════════════════════════════════════════════════")
                print("    Action CANCELED. Student Record NOT Saved.    ")
                print("════════════════════════════════════════════════════") 
        else:
            print("")
            print("╔══════════════════════════════════════════════════╗")
            print("║        ERROR! No file is currently open.         ║")
            print("║            Please OPEN a file first.             ║")
            print("╚══════════════════════════════════════════════════╝")
    
    # This lets the user to save the records to a new file
    elif choice == "3":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║            CURRENT OPTION: Save As File          ║")
        print("╚══════════════════════════════════════════════════╝")
        filename = input("Enter new filename: ").lower()
        save_records(filename)
    
    # This lets the user to show all student records
    elif choice == "4":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║     CURRENT OPTION: Show All Student Records     ║")
        print("╚══════════════════════════════════════════════════╝")
        print("")
        if not student_records:
            print("")
            print("╔══════════════════════════════════════════════════╗")
            print("║         ERROR! No Student Records Found.         ║")
            print("╚══════════════════════════════════════════════════╝")
        else:
            # Sorting Menu
            print("╔═════════════════════════════════════════════╗")
            print("║           SHOW ALL: Sorting Menu            ║")
            print("╠═════════════════════════════════════════════╣")
            print("║ MENU OPTIONS          **select an option**  ║")
            print("║  [1] - Last Name (A-Z)                      ║")
            print("║  [2] - Final Grade (Ascending)              ║")
            print("║  [3] - Final Grade (Descending)             ║")
            print("║  [0] - No Sorting                           ║")
            print("╚═════════════════════════════════════════════╝")
            sort_option = input("Enter your choice: ")

            if sort_option == "1":
                sorted_records = sorted(student_records, key=lambda x: x[3])  # Sort by Last Name
                print("╔═════════════════════════════════════════════╗")
                print("║          SORTED: Last Name (A-Z)            ║")
                print("╚═════════════════════════════════════════════╝")
            elif sort_option == "2":
                sorted_records = sorted(student_records, key=lambda x: x[6])  # Sort by Final Grade
                print("╔═════════════════════════════════════════════╗")
                print("║        SORTED: Final Grade (Ascending)      ║")
                print("╚═════════════════════════════════════════════╝")
            elif sort_option == "3":
                sorted_records = sorted(student_records, key=lambda x: x[6], reverse=True)  # Sort by Final Grade (Descending)
                print("╔═════════════════════════════════════════════╗")
                print("║       SORTED: Final Grade (Descending)      ║")
                print("╚═════════════════════════════════════════════╝")
            else:
                sorted_records = student_records  # No sorting

        for record in sorted_records:
            print(f"Full Name      : {record[3]}, {record[2]}")
            print(f"ID             : {record[0]}")
            print(f"Class Standing : {record[4]}")
            print(f"Exam Grade     : {record[5]}")
            print(f"Final Grade    : {record[6]}")
            print("")
        
        print("═══════════════════════END══════════════════════════")

    # This lets the user to show and search a student record
    elif choice == "5":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║    CURRENT OPTION: Show/Search Student Record    ║")
        print("╚══════════════════════════════════════════════════╝")
        student_id = input("Enter Student ID to search: ")
        print("Searching for Student", student_id + "...")
        found = False
        for record in student_records:
            if record[0] == student_id:
                print("╔══════════════════════════════════════════════════╗")
                print("║              STUDENT RECORD FOUND!               ║")
                print("╚══════════════════════════════════════════════════╝")
                print(f"ID             : {record[0]}")
                print(f"Full Name      : {record[3]}, {record[2]}")
                print(f"Class Standing : {record[4]}")
                print(f"Exam Grade     : {record[5]}")
                print(f"Final Grade    : {record[6]}")
                print("════════════════════════════════════════════════════")
                found = True
                break
        if not found:
            print("")
            print("╔══════════════════════════════════════════════════╗")
            print("║         SORRY! Student Record Not Found.         ║")
            print("║                        :(                        ║")
            print("╚══════════════════════════════════════════════════╝")
    elif choice == "6":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║            CURRENT OPTION: Add Record            ║")
        print("╚══════════════════════════════════════════════════╝")
        student_id = input("Student ID (6 digits) : ").strip()
        firstname = input("Student First Name    : ").strip().upper()
        lastname = input("Student Last Name     : ").strip().upper()
        class_standing = input("Class Standing /100   : ").strip()
        exam_grade = input("Major Exam Grade /100 : ").strip()
        student_fname = (firstname + " " + lastname).upper()
        final_grade = int((float(class_standing) * 0.6) + (float(exam_grade) * 0.4))
        student_records.append((student_id, student_fname, firstname, lastname, class_standing, exam_grade, final_grade))
        print("════════════════════════════════════════════════════")
        print("          Student Record added successfully!        ")
        print("════════════════════════════════════════════════════")
    
    # This lets the user to edit an existing a student record
    elif choice == "7":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║           CURRENT OPTION: Edit Record            ║")
        print("╚══════════════════════════════════════════════════╝")
        student_id = input("Search Student ID to EDIT: ")
        print("Searching for Student", student_id + "...")
        for i, record in enumerate(student_records):
            if record[0] == student_id:
                print("╔══════════════════════════════════════════════════╗")
                print("║          EXISTING STUDENT RECORD FOUND!          ║")
                print("╚══════════════════════════════════════════════════╝")
                print(f"ID             : {record[0]}")
                print(f"Full Name      : {record[3]}, {record[2]}")
                print(f"Class Standing : {record[4]}")
                print(f"Exam Grade     : {record[5]}")
                print(f"Final Grade    : {record[6]}")
                print("════════════════════════════════════════════════════")
                print("")
                
                print("╔══════════════════════════════════════════════════╗")
                print("║             EDITING STUDENT RECORD...            ║")
                print("╚══════════════════════════════════════════════════╝")
                student_id = input("Student ID (6 digits) : ").strip()
                firstname = input("Student First Name    : ").strip().upper()
                lastname = input("Student Last Name     : ").strip().upper()
                class_standing = input("Class Standing /100   : ").strip()
                exam_grade = input("Major Exam Grade /100 : ").strip()
                student_fname = (firstname + " " + lastname).upper()
                final_grade = int((float(class_standing) * 0.6) + (float(exam_grade) * 0.4))
                student_records[i] = (student_id, student_fname, firstname, lastname, class_standing, exam_grade, final_grade)
                print("════════════════════════════════════════════════════")
                print("  Student Record UPDATED and EDITED Successfully!   ")
                print("════════════════════════════════════════════════════")
                break
        else: 
            print("════════════════════════════════════════════════════")
            print("          Oh no! Student Record NOT FOUND.          ")
            print("                       :(                           ")
            print("════════════════════════════════════════════════════")
            
    
    # This lets the user to delete an existing a student record
    # It also ask for final CONFIRMATION before deleting
    elif choice == "8":
        print("")
        print("╔══════════════════════════════════════════════════╗")
        print("║          CURRENT OPTION: Delete Record           ║")
        print("╚══════════════════════════════════════════════════╝")
        student_id = input("Search Student ID to DELETE: ")
        print("Searching for Student", student_id + "...")
        for i, record in enumerate(student_records):
            if record[0] == student_id:
                print("╔══════════════════════════════════════════════════╗")
                print("║          EXISTING STUDENT RECORD FOUND!          ║")
                print("╚══════════════════════════════════════════════════╝")
                print(f"ID             : {record[0]}")
                print(f"Full Name      : {record[3]}, {record[2]}")
                print(f"Class Standing : {record[4]}")
                print(f"Exam Grade     : {record[5]}")
                print(f"Final Grade    : {record[6]}")
                print("════════════════════════════════════════════════════")
                
                # Ask for final confirmation before deleting
                print("")
                print("Are you sure you want to DELETE this record?")
                print("NOTE: This action CANNOT be undone. (yes/no)")
                print("")
                confirm = input("Confirm? : ").strip().lower()
            
                if confirm == "yes":
                    del student_records[i]  # Remove record from the list
                    print("════════════════════════════════════════════════════")
                    print("        Student Record DELETED SUCCESSFULLY!        ")
                    print("════════════════════════════════════════════════════")
                else:
                    print("════════════════════════════════════════════════════")
                    print("    Action CANCELED. Student Record NOT Deleted.    ")
                    print("════════════════════════════════════════════════════")
                break  
        else: 
            print("════════════════════════════════════════════════════")
            print("          Oh no! Student Record NOT FOUND.          ")
            print("                       :(                           ")
            print("════════════════════════════════════════════════════")
    
    else:
        print("Invalid choice. Please try again.")
    
    # A pause for every iteration in menus :)
    input("Press ENTER to continue...") 
    print("")
    
    # end of the program :)
# code ends HERE!!! yey!