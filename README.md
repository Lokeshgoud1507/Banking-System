Banking-System-
Project from iit mandi code as following:- 10-130 (https://youtu.be/ogGPidb4pxY?si=V7lFAkBdn776RkLt)

import os import datetime

File paths
ACCOUNTS_FILE = "accounts.txt" TRANSACTIONS_FILE = "transactions.txt"

Helper functions

def log_transaction(account_number, transaction_type, amount): """Log a transaction in transactions.txt.""" date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") with open(TRANSACTIONS_FILE, "a") as file: file.write(f"{account_number},{transaction_type},{amount},{date}\n")

def generate_account_number(): """Generate a unique account number.""" return str(100000 + len(load_accounts()))

Main menu functions

def create_account(): print("\nCREATING AN ACCOUNT") name = input("Enter your name: ") initial_deposit = float(input("Enter your initial deposit: ")) account_number = generate_account_number() password = input("Enter a password: ") save_account(account_number, name, password, initial_deposit) print(f"Account created successfully! Your account number is: {account_number}")

def login(): print("\nLOGGING IN") accounts = load_accounts() account_number = input("Enter your account number: ") password = input("Enter your password: ")

if account_number in accounts and accounts[account_number]["password"] == password:
    print("Login successful!")
    logged_in_menu(account_number, accounts)
else:
    print("Invalid account number or password.")
def logged_in_menu(account_number, accounts): while True: print("\n1) Deposit") print("2) Withdraw") print("3) Logout") choice = input("Enter your choice: ")

    if choice == "1":
        deposit(account_number, accounts)
    elif choice == "2":
        withdraw(account_number, accounts)
    elif choice == "3":
        print("Logged out successfully!")
        break
    else:
        print("Invalid choice, try again.")
def deposit(account_number, accounts): amount = float(input("Enter amount to deposit: ")) accounts[account_number]["balance"] += amount save_accounts(accounts) log_transaction(account_number, "Deposit", amount) print(f"Deposit successful! Current balance: {accounts[account_number]['balance']}")

def withdraw(account_number, accounts): amount = float(input("Enter amount to withdraw: ")) if accounts[account_number]["balance"] >= amount: accounts[account_number]["balance"] -= amount save_accounts(accounts) log_transaction(account_number, "Withdrawal", amount) print(f"Withdrawal successful! Current balance: {accounts[account_number]['balance']}") else: print("Insufficient balance.")

def save_accounts(accounts): """Save all accounts back to accounts.txt.""" with open(ACCOUNTS_FILE, "w") as file: for acc_num, details in accounts.items(): file.write(f"{acc_num},{details['name']},{details['password']},{details['balance']}\n")

def main(): while True: print("\nMAIN MENU") print("Welcome to the bank system!") print("1) Create account") print("2) Login") print("3) Exit") choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank you for using the bank system. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
Run the program
if name == "main": main()
