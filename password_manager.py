import csv
import random

# 1. View Stored Accounts
def read_accounts():
    try:
        with open("accounts.csv", "r", newline="") as f:
            accounts_reader = csv.DictReader(f)
            return list(accounts_reader)
        
    except FileNotFoundError:
        with open("accounts.csv", "w", newline="") as f:
            accounts_writer = csv.DictWriter(f, field_names)
            accounts_writer.writeheader()
            accounts_writer.writerow({'account': 'default', 'username' : 'default', 'password' : 'password1234', 'strength' : 'weak'})
            return []
        
    except PermissionError:
        print("You do not have the proper permissions for this file.")
        return []


# 2. Store account credentials
field_names=['account', 'username', 'password', 'strength']

def add_account(account, username, password):
    try:
        
        strength = check_password_strength(password)
        
        if strength == "Weak":
            while strength == "Weak":
                print(f"WARNING {password} is a weak password.")
                change = input("Do you want to change it? (yes/no)").lower()
                if change == "yes":
                    password = input("What is your new password: ")
                    strength = check_password_strength(password)
                elif change == "no":
                    break

        elif strength == "Medium":
            print("This password has medium strength")

        elif strength == "Strong":
            print("Good choice of password. This is strong!")
                
        with open("accounts.csv", "a", newline="") as f:
            accounts_writer = csv.DictWriter(f, field_names)
            accounts_writer.writerow({'account': account, 'username' : username, 'password' : password, 'strength' : strength})

    except Exception as e:
        print(f"Failed to add account: {e}")


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
    
def search_for_account(account):
    accounts_list = read_accounts()

    for account_dict in accounts_list:
        if account.lower() == account_dict['account'].lower():
            return account_dict['password']
        
    return "Account not found"


def generate_password(length=int):

    # From a string of the alphabet special characters and numbers, loop through however many times length is. 
    # Append to end of password
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    specialchars = "@#~!%^&*(())"
    password = ""

    while len(password) < length:
        password = password + random.choice(alpha)
        password = password + random.choice(nums)
        password = password + random.choice(specialchars)
    
    return password


# 3. Add a menu
def menu():
    print("Welcome to Pperk's Pass Man")
    while True:
        print("Make your selection: \n" \
        "1. View accounts \n" \
        "2. Add account \n" \
        "3. Search for Account \n" \
        "4. Quit")
        x = int(input("What is your choice: "))
        print("-------------")
        if x == 1:
            show_accounts()
        elif x == 2:
            account = input("What is the account: ")
            username = input("What is the username: ")
            user_random = input("Do you want a random password? (yes/no)").lower()
            
            if user_random == "yes":
                length = int(input("How long do you want it? (12 is strong): "))
                password = generate_password(length)
            elif user_random == "no":
                password = input("What is the password: ")
            add_account(account, username, password)
        elif x == 3:
            account = input("What is the account: ")
            password = search_for_account(account)
            print(f"Account: {account} | Password: {password}")
        elif x == 4:
            print("Thank you for securing your passwords. Goodbye!")
            break
        print("-------------")
menu()