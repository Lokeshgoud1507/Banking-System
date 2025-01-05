
import random
import os
import hashlib
from datetime import datetime

ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def read_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath,'w') as f:
            pass
    with open(filepath,'r') as f:
        return f.readlines()


def write_to_file(filepath,data,mode='a'):
    with  open(filepath,mode) as f:
        f.write(data + "\n")


def generate_account_number():
    return str(datetime.now().strftime('%Y%m%d%H%M%S'))



def create_account():
    print("\n===Create Account===")
    name = input("enter your name")
    initial_deposit = float(input("Enter your initial deposit"))
    password= input("enter you password")

    account_number= generate_account_number()
    hashed_password = hash_password(password)

    account_data = f"{account_number},{name},{hashed_password},{initial_deposit}"
    write_to_file(ACCOUNTS_FILE,account_data)

    print(f"Account created successfully! Your account number is {account_number}")

def login():

    print("\n ===Login===")
    account_number = input("Enter your account number")
    password = input("Enter your Password")
    hashed_password = hash_password(password)

    accounts = read_file(ACCOUNTS_FILE)
    for account in accounts:
        acc_no,name,acc_password ,balance = account.strip().split(',')
        if acc_no == account_number and acc_password == hashed_password:
            print("Login Successful!\n")
            perform_transactions(account_number,float(balance))
            return
    print("Invalid Account number or password. \n")

def perform_transactions(account_number,balance):
    while True:
        print("\n===Banking Menu===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transactions History")
        print("5. Logout")
        choice = input("Enter your choice : ")

        if choice == "1":
            print(f"your current balance is : ",balance)
        elif choice == "2":
            amount = float(input("enter amount to deposit"))
            balance += amount
            log_transaction(account_number,"Deposit",amount)
            update_account_balance(account_number,balance)
            print(f"Deposit successful! New balance :{balance}\n")
        elif choice == "3":
            amount = float(input('enter amount to withdraw'))
            if amount>balance:
                print("Insufficient balance")
            else:
                balance -=amount
                log_transaction(account_number, "Withdrawl", amount)
                update_account_balance(account_number,balance)
                print(f"Withdrawl successful New balance : {balance} \n")

        elif choice == "4":
            view_transaction_history(account_number)
        elif choice == "5":
            print("Logged out successfully . \n")
            break
        else:
            print("Invalid Choice. Try again. \n")

def log_transaction(account_number , transaction_type , amount):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_data = f"{account_number},{transaction_type},{amount},{date}"
    write_to_file(TRANSACTIONS_FILE,transaction_data)

def update_account_balance(account_number , newbalance):
    accounts = read_file(ACCOUNTS_FILE)
    update_accounts = []
    for account in accounts:
        acc_no, name, password, balance = account.strip().split(',')
        if acc_no == account_number:
            update_accounts.append(f"{acc_no},{name},{password},{newbalance}")
        else:
            update_accounts.append((account.strip()))
    with open(ACCOUNTS_FILE,"w") as f:
        f.write("\n".join(update_accounts)+"\n")

def view_transaction_history(account_number):
    print("\n === Transaction History")
    transactions = read_file(TRANSACTIONS_FILE)
    for transaction in transactions:
        acc_no, transaction_type, amount, date = transaction.strip().split(',')
        if acc_no == account_number:
            print(f"{transaction_type}:{amount} on  {date}")
    print()


def main():
    while True:
        print("\n === Banking System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice  == "3":
            print("Thank You 🙏 for using Banking System. GoodBye! 👋")
            break
        else:
            print("Invalid Code .Try again.\n")

if __name__ =="__main__":
    main()

