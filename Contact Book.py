class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    def __str__(self):
        return f"Store Name: {self.store_name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []
    def add_contact(self, store_name, phone_number, email, address):
        new_contact = Contact(store_name, phone_number, email, address)
        self.contacts.append(new_contact)
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.store_name.lower() or search_term in contact.phone_number]
        if not found_contacts:
            print(f"No contacts found for '{search_term}'.")
        else:
            print("\n--- Search Results ---")
            for contact in found_contacts:
                print(contact)
    def update_contact(self, index, store_name=None, phone_number=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            if store_name:
                contact.store_name = store_name
            if phone_number:
                contact.phone_number = phone_number
            if email:
                contact.email = email
            if address:
                contact.address = address
            print("Contact updated successfully.")
        else:
            print("Invalid index.")
    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid index.")
def display_menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def contact_management_system():
    manager = ContactManager()
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(store_name, phone_number, email, address)
            print("Contact added successfully.")
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter store name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == "4":
            manager.view_contacts()
            try:
                contact_index = int(input("Enter the number of the contact to update: ")) - 1
                store_name = input("Enter new store name (leave empty to keep current): ")
                phone_number = input("Enter new phone number (leave empty to keep current): ")
                email = input("Enter new email (leave empty to keep current): ")
                address = input("Enter new address (leave empty to keep current): ")
                manager.update_contact(contact_index, store_name, phone_number, email, address)
            except ValueError:
                print("Invalid input, please enter a valid number.")
        elif choice == "5":
            manager.view_contacts()
            try:
                contact_index = int(input("Enter the number of the contact to delete: ")) - 1
                manager.delete_contact(contact_index)
            except ValueError:
                print("Invalid input, please enter a valid number.")
        elif choice == "6":
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid choice, please try again.")
contact_management_system()
