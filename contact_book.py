# Contact Book Application (CLI)

import json
import os

file_name = "contacts.json"

# -------- Load contacts from file --------
def load_contacts():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return []

# -------- Save contacts --------
def save_contacts():
    with open(file_name, "w") as f:
        json.dump(contact_list, f)

# -------- Add new contact --------
def add_contact():
    print("\nEnter Contact Details")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    if name == "" or phone == "":
        print("Name and Phone are required!\n")
        return

    contact_list.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts()
    print("Contact added successfully!\n")

# -------- View all contacts --------
def view_contacts():
    if len(contact_list) == 0:
        print("\nNo contacts found.\n")
        return

    print("\nContact List:")
    for i in range(len(contact_list)):
        print(f"{i+1}. {contact_list[i]['name']} - {contact_list[i]['phone']}")
    print()

# -------- Search contact --------
def search_contact():
    search = input("Enter name or phone to search: ").lower()

    found = False
    for contact in contact_list:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            print()
            found = True

    if not found:
        print("No matching contact found.\n")

# -------- Update contact --------
def update_contact():
    view_contacts()
    try:
        num = int(input("Enter contact number to update: "))
        contact = contact_list[num - 1]

        print("Leave blank to keep old value")

        new_name = input("New Name: ").strip()
        new_phone = input("New Phone: ").strip()
        new_email = input("New Email: ").strip()
        new_address = input("New Address: ").strip()

        if new_name != "":
            contact["name"] = new_name
        if new_phone != "":
            contact["phone"] = new_phone
        if new_email != "":
            contact["email"] = new_email
        if new_address != "":
            contact["address"] = new_address

        save_contacts()
        print("Contact updated successfully!\n")

    except:
        print("Invalid selection!\n")

# -------- Delete contact --------
def delete_contact():
    view_contacts()
    try:
        num = int(input("Enter contact number to delete: "))
        removed = contact_list.pop(num - 1)
        save_contacts()
        print(f"Contact '{removed['name']}' deleted successfully!\n")
    except:
        print("Invalid selection!\n")


# -------- Main Program --------
contact_list = load_contacts()

while True:
    print("====== CONTACT BOOK MENU ======")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please try again.\n")