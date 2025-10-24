import csv


# 1. View Stored Accounts
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
            accounts_writer.writerow({'account': 'default', 'username' : 'default', 'password' : 'password1234', 'strength' : 'weak'})
    except PermissionError:
        print("You do not have the proper permissions for this file.")


# 2. Store account credentials
field_names=['account', 'username', 'password', 'strength']
def add_account(account, username, password):
    try:
        
        strength = check_password_strength(password)

        if strength == "Weak":
            print(f"WARNING {password} is a weak password.")
            change = input("Do you want to change it? ")
            if change == "Yes":
                password = input("What is your new password: ")
            elif change == "No" or change == "":
                password = password
        elif strength == "Medium":
            print("This password has medium strength")
        elif strength == "Strong":
            print("Good choice of password. This is strong!")
        
        
        with open("accounts.csv", "a", newline="") as f:
            accounts_writer = csv.DictWriter(f, field_names)
            accounts_writer.writerow({'account': account, 'username' : username, 'password' : password, 'strength' : strength})


    except:
        pass


def show_accounts():
    accounts=read_accounts()
    print("Account | Username | Password | Strength")
    for row in accounts:
        print(f"{row['account']} | {row['username']} | {row['password']} | {row['strength']}")
    

def check_password_strength(password):
    checks=0
    # Check password length
    passlength = len(password)

    #Create check for uppercase
    if any(char.isupper() for char in password):
        checks=checks+1
    #Create check for lowercase
    if any(char.islower() for char in password):
        checks=checks+1
    #Create check for number
    if any(char.isdigit() for char in password):
        checks=checks+1
    #Create check for special character
    if any(not char.isalnum() for char in password):
        checks=checks+1

    # If password length >= 12 has uppercase, lowercase, number, and special character = strong
    if passlength >=12 and checks==4:
        return("Strong")
    # If password length >= 8 has atleast 3 
    elif passlength >= 8 & checks>=3:
        return("Medium")
    # Else false
    else:
        return("Weak")
    

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