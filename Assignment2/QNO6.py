# 6. Contact Book (Dictionary)
# Write a Python program that:
# ● Creates a dictionary to store contacts (name → phone number).
# ● Allows the user to:
# ○ Add a new contact
# ○ Update a contact’s number
# ○ Delete a contact
# ○ Search a contact by name

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added")

    elif choice == 2:
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact updated")
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
