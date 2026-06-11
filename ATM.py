# ATM Simulation System

balance = 0
transactions = []


def deposit():
    global balance

    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        balance += amount
        transactions.append(f"Deposited ₹{amount}")

        print(f"₹{amount} deposited successfully.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            transactions.append(f"Withdrawn ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


def check_balance():
    print(f"\nCurrent Balance: ₹{balance}")


def show_transaction_history():

    if len(transactions) == 0:
        print("\nNo transactions found.")
    else:
        print("\n----- Transaction History -----")

        for transaction in transactions:
            print(transaction)


def menu():

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Transaction History")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                deposit()

            elif choice == 2:
                withdraw()

            elif choice == 3:
                check_balance()

            elif choice == 4:
                show_transaction_history()

            elif choice == 5:
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid choice! Please select 1-5.")

        except ValueError:
            print("Please enter a valid number.")


menu()