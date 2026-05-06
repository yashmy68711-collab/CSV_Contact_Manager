import csv
import os

FILE_NAME = "contacts.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone"])

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()

        if name == "" or phone == "":
            print("Invalid input")
        else:
            with open(FILE_NAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, phone])

            print("Contact saved!")

    # View contacts
    elif choice == "2":
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\nContacts:")
            for row in reader:
                print(row[0], "-", row[1])

    # Exit
    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Wrong choice")