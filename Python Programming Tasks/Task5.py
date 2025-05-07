# Contact Management System Program.This program allows users to create, view, search, and delete contacts. It also saves the contacts to a CSV file.The program uses a list of dictionaries to store contact information and the csv module to handle CSV files.

import csv # importing the csv module to handle CSV files.


def create_contact(contacts):
    
    try:
        
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        
        if not validate_phone_number(phone):
            pass  # Re-prompt user for valid phone number
        
        email = input("Enter email: ")
        address = input("Enter address: ")
        print("\n")
    
    except ValueError:
        
        print("Invalid input! Please enter valid data.")
        print("\n")
        create_contact(contacts) # Restart the create function.
    
    for contact in contacts:
        
        if contact["Phone"] == phone:
            
            print("A contact with this number already exists. Please enter a unique contact.")
            print("\n")
            return  # Exit without saving
        
    contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
    
    contacts.append(contact)
    
    with open('contactslist.csv', 'a', newline='') as f:
            
            writer = csv.DictWriter(f, fieldnames=contact.keys())
            
            if f.tell() == 0: # Check if the file is empty to write the header.
                
                writer.writeheader()
                
            writer.writerow(contact)

    print("Contact saved successfully!")
    print("\n")


def validate_phone_number(phone):
    
    #Validates if the phone number is exactly 10 digits.
    
    if len(phone) != 10 or not phone.isdigit():
        
        print("Error: Phone number must be exactly 10 digits and contain only numbers.")
        print("\n")
        
        return False
    
    return True


def view_contacts(contacts):
    
    if len(contacts) == 0:
        
        print("No contacts found.")
        print("\n")
        
    else:
        
        print("Your contacts are:")
        print("\n")
        
        for contact in contacts:
                
            print("Name:", contact['Name'])
            print("Phone:", contact['Phone'])
            print("Email:", contact['Email'])
            print("Address:", contact['Address'])
            print("\n")


def search_contact(contacts):
    
    try:
        
        num = input("Enter the number of the contact to search: ")
        print("\n")
        
        if not validate_phone_number(num):
            return  # Re-prompt user for valid phone number
        
    except ValueError:
        
        print("Invalid input! Please enter a valid number.")
        print("\n")
        return # Exit the function if the input is invalid.
        
    found = False
    
    for contact in contacts:
        
        if str(contact["Phone"]) == num:
            
            print("Contact found:")
            print("\n")
            print("1. Name:", contact['Name'])
            print("2. Phone:", contact['Phone'])
            print("3. Email:", contact['Email'])
            print("4. Address:", contact['Address'])
            print("\n")
            found = True
            break
    
    if found == False:
        
        print("Contact not found. Please enter a valid contact number.")
        print("\n")
        

def delete_contact(contacts):
    
    try:
        
        num = input("Enter the number of the contact to delete: ")
        print("\n")
        
        if not validate_phone_number(num):
            return  # Re-prompt user for valid phone number
    
    except ValueError:
        
        print("Invalid input! Please enter a valid number.")
        print("\n")
        return # Exit the function if the input is invalid.
    
    for contact in contacts:
        
        if str(contact["Phone"]) == num:
            
            contacts.remove(contact)
            print(f"Contact {contact['Name']} deleted successfully!")
            print("\n")
            
            with open('contactslist.csv', 'w', newline='') as f:
                
                writer = csv.DictWriter(f, fieldnames=contact.keys())
                writer.writeheader()
                writer.writerows(contacts)
 
            break
        
        else:
                
                print(f"Contact with number ({num}) not found. Please enter a valid contact number.")
                print("\n")


def update_contact(contacts):
    
    try:
        
        num = input("Enter the number of the contact to update: ")
        print("\n")
        
        if not validate_phone_number(num):
            return  # Re-prompt user for valid phone number
        
    except ValueError:
        
        print("Invalid input! Please enter a valid number.")
        print("\n")
        return # Exit the function if the input is invalid.
    
    found = False
    
    for contact in contacts:
        
        if str(contact["Phone"]) == num:
            
            found = True
            
            print("Current contact details are:")
            print("\n")
            print("1. Name:", contact['Name'])
            print("2. Phone:", contact['Phone'])
            print("3. Email:", contact['Email'])
            print("4. Address:", contact['Address'])
            print("\n")
            
            # Asks user for new values.
            
            print("Enter new values (or press Enter to keep the same):") 
            print("\n")
            
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            
            if name:
                
                contact['Name'] = name
            
            if phone:
                if validate_phone_number(phone):
                    contact['Phone'] = phone
                
            if email:

                contact['Email'] = email

            if address:
                
                contact['Address'] = address
                
            print("Contact updated successfully!")
            print("\n")
            
            with open('contactslist.csv', 'w', newline='') as f:
                
                writer = csv.DictWriter(f, fieldnames=contact.keys())
                writer.writeheader()
                writer.writerows(contacts)
            
            print("Contact updated successfully!")
            print("\n")
            
            break
    
    if found == False:
        
        print(f"Contact with number {num} not found.")
        print("\n")
        
 
def load_contacts():
    
    try:
        
        with open('contactslist.csv', 'r') as f:
            
            reader = csv.DictReader(f)
            contacts = list(reader) # Read contacts from CSV file.
            
    except FileNotFoundError:
        
        contacts = [] # Initialize an empty list if no file is found.
    
    return contacts
 
        
def main():
        
        contacts = load_contacts() # Loads the stored contacts.
            
        while True:
            
            print("Welcome to the Contact Management System!")
            print("\n")
            print("Select an option:")
            print("\n")
            print("1. Create contact")
            print("2. View contacts")
            print("3. Search contact")
            print("4. Delete contact")
            print("5. Update contact")
            print("6. Exit")
            print("\n")
            
            choice = input("Enter your choice (1-6): ")
            print("\n")
            
            if choice == '1':
                
                create_contact(contacts)
                
            elif choice == '2':
                
                view_contacts(contacts)
                
            elif choice == '3':
                
                search_contact(contacts)
                
            elif choice == '4':
                
                delete_contact(contacts)
                
            elif choice == '5':
                
                update_contact(contacts)
                
            elif choice == '6':
                
                print("Thank you for using the Contact Management System!")
                print("Goodbye!")
                print("\n")
                break
            
            else:
                
                print("Invalid choice! Please enter a valid option.")
                print("\n")


if __name__ == "__main__":
        
        main() # Start the program.