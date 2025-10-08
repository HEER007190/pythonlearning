inventory = []
def add_inventory(item, quantity, total_price):
    inventorys = {"Item": item, "Quantity": quantity, "Total_price": total_price}
    inventory.append(inventorys)
    print(f"{item} added to inventory{quantity} of {total_price}")

def show_inventory():
    if not inventory:
        print("Inventory is empty")
    else:
        for i, item in enumerate(inventory):
            print(f"{i + 1}. {item['Item']} with {item['Quantity']} of {item['Total_price']}")

def search_inventory(item):
    for inventorys in inventory:
        if item['Item'] == inventorys['Item']:
            print(f"{inventorys['Item']} is in inventory with {item['Quantity']} of {item['Total_price']}")
        else:
            print(f"{inventorys['Item']} is not in inventory")

owner_choice = input("Would you like to open inventory management system?: ").title().strip()
if owner_choice == "Yes":
    print("Welcome to Inventory Management System")
    while True:
        print("Which Function would you like to use?:")
        print("Add item")
        print("Show Inventory")
        print("Search Inventory")
        print("Exit")
        owner_option = input("Which Function would you like to use:").title().strip()
        if owner_option == "Add Item":
            add_inventory(input("Enter Item Name: "), int(input("Enter Item quantity: ")),
                          int(input("Enter Item total_price: ")))
        elif owner_option == "Show Inventory":
            show_inventory()

        elif owner_option == "Search Inventory":
            search_inventory(input("Enter Item Name: "))

        elif owner_option == "Exit":
            print("Thank you for using Inventory Management System")
            break

        else:
            print("Invalid choice")

elif owner_choice == "No":
    print("Thank you for visiting Inventory Management System")
    exit()

else:
    print("Please enter a valid choice")