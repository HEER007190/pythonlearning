pin=000000
balance=50000
total_balance=0
user_pin=int(input("Enter your PIN: "))
while True:
 if user_pin == pin:
     user_choice = input("What you want to choice? ").title().strip()
     if user_choice == "Withdraw":
        withdraw_balance=int(input("Enter your amount to withdraw: "))

        if withdraw_balance <= balance:
            print("Amount succesfully withdrawn")
            total_balance = balance - withdraw_balance
            print('Your balance is now ', total_balance)
        else:
            print("You don't have enough money")
        if user_choice == "Deposit":
            deposit_balance=int(input("Enter your amount to deposit: "))
            total_balance=balance + deposit_balance
            print('Your balance is now ', total_balance)
        if user_choice == "Check balance":
            print("Your balance is now ", total_balance)
        if user_choice == "Exit":
         break
        user_operation = input("What do you want to do yes or no ").title().strip()
        if user_operation == "No":
            print("Thank you for using ATM")
            break
 else:
    print("Wrong PIN")