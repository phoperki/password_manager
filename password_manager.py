import csv
# 1. Store account credentials
field_names=['account', 'username', 'password']
def add_account(account, username, password):
    try:
        with open("accounts.csv", "a", newline="") as f:
            accounts_writer = csv.DictWriter(f, field_names)
            accounts_writer.writerow({'account': account, 'username' : username, 'password' : password})
    except:
        pass

# 2. View Stored Accounts
def read_accounts():
    try:
        with open("accounts.csv", "r", newline="") as f:
            accounts_reader = csv.DictReader(f)
            accounts = accounts_reader
            return list(accounts)
    except FileNotFoundError:
        with open("accounts.csv", "w", newline="") as f:
            accounts_writer = csv.DictWriter(f, field_names)
            accounts_writer.writeheader()
            accounts_writer.writerow({'account': 'default', 'username' : 'default', 'password' : 'password1234'})
    except PermissionError:
        print("You do not have the proper permissions for this file.")


def show_accounts():
    accounts=read_accounts()
    print("Account | Username | Password")
    for row in accounts:
        print(f"{row['account']} | {row['username']} | {row['password']}")
    

# 3. Add a menu
def menu():
    print("Welcome to Pperk's Pass Man")
    while True:
        print("Make your selection: \n" \
        "1. View accounts \n" \
        "2. Add account \n" \
        "3. Quit")
        x = int(input("What is your choice: "))
        if x == 1:
            show_accounts()
        elif x == 2:
            account = input("What is the account: ")
            username = input("What is the username: ")
            password = input("What is the password: ")
            add_account(account, username, password)
        elif x == 3:
            print("Thank you for securing your passwords. Goodbye!")
            break

menu()