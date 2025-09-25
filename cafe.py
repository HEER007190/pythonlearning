
def cafe():
    menu = {
        "Cheesy Pizza": 150,
        "Aloo Tikki Burger": 50,
        "Coke": 20,
        "White Sauce Pasta": 250,
        "Veg Sandwich": 60,
        "French Fries": 80,
        "Cold Coffee": 70,
        "Chocolate Cake": 120,
        "Spring Rolls": 90,
        "Pasta Arabia": 200
    }
    print("\n Cafe Menu")
    for item, price in menu.items():  #.item() is necessary to print things present in dictionary one bye one
        print(item, ":₹", price)
    total = 0
    cust = ["Order Now", "Done"]
    cust_choice = input("Would you like to order now or you are done:".strip().upper())
    if cust_choice == "ORDER NOW":
        while True:
            cust_order = str(input("Customer Order is :".strip().upper()))
            price = menu[cust_order]
            print("Price of", cust_order, "is", price)
            total += price
            cust_dec = ["ORDER AGAIN", "DONE"]
            cust_dic = str(input("Would you like to order more or done :".strip().upper()))
            if cust_dic == "ORDER AGAIN":
                cust_order = str(input("Customer Order is :".strip().upper()))
                price = menu[cust_order]
                total += price
                print("Price of", cust_order, "is", price)
            elif cust_dic == "DONE":
                break
            else:
                print("Invalid choice")
            if cust_order in menu:
                print(f"you ordered {cust_order} priced at {menu[cust_order]}")
            else:
                print("Order Not Found")

    print("Your Bill is ₹:", total)
    print("Thank you for visiting our cafe")


cafe()
