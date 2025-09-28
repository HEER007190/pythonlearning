contacts=[]
def add_contact(name,phone):
    contact={"name":name,"phone":phone}
    contacts.append(contact)
    print(f"Added contact {name} with phone {phone} successfully")

def show_contacts():
    if not contacts:
        print("No contacts added")
    else:
        print("Contacts list")
        for i ,contact in enumerate(contacts):
            print(f"{i}. {contact['name']} with phone {contact['phone']}")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"{contact['name']} with phone {contact['phone']}")
        else:
            print("Contact not found")

User=input("Whould you like to open your contact list?? ").title().strip()
if User == "Yes":
 print("Contact list")
 while True:
    print("Select options:")
    print("Add Contact")
    print("show Contacts")
    print("Search Contact")
    print("Exit")
    user_input = input("Enter your choice: ").title().strip()
    if user_input == "Add Contact":
        add_contact(input("Enter Contact Name: "),input("Enter Contact Phone: "))
    elif user_input == "show Contacts":
        show_contacts()
    elif user_input == "Search Contact":
        search_contact(input("Enter Contact Name: "))
    elif user_input == "Exit":
        print("Thank you for using this program")
        exit()
    else:
        print("Invalid input")
else:
    print("We Hope You like it")