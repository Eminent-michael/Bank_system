import random
import time
import pandas as pd
from backend import Account


dat = Account()
print(dat.all_info())
dat.commit()

print("What would like us to do for you today?")
print(" ")
print("Enter '1' to Create Account.")
print("Enter '2' to Deposit Money.")
print("Enter '3' to Withdraw money.")
print("Enter '4' to Transfer.")
print("Enter '5' to Check Account Balance.")

customer_input = int(input("> "))
data = Account()

# Create account line of code......

if int(customer_input) == 1:
    name = input("Enter your name: ")
    while len(name) == 0:
        name = input("Enter your name: ")

    email = input("Enter your email: ")

    # This pick 6-digit number in random and check
    # if it exists in the account_list.txt it reruns the code (it's a while loop)
    # if it does then save the code in the account_list.txt file and print to save to database.

    while True:
        account_no = random.randint(100000, 999999)
        ap = []
        file = pd.read_fwf("account_list.txt", header=None)
        all_list = list(file.loc[:, 0])
        if account_no in all_list:
            time.sleep(1)
        else:
            ap.append(account_no)
            df = pd.DataFrame(ap)
            df.to_csv("account_list.txt", mode="a", header=None, index=None)
            print("Jesus!!!")
            break

    print(f"Please write down your account number '{account_no}', its only show once.")

    pin = input("Enter the 4 digit for your pin: ")

    while len(pin) > 4 or len(pin) < 4:
        pin = input("Enter the 4 digit for your pin: ")
    print(pin)
    data.create_account(name, email, account_no, pin)
    data.commit()
    print(f"""
    This is a one time message.\n
    Your name is {name}
    Your account number '{account_no}'\n
    Your pin is '{pin}'.\n
    Thank you for using our bank.
    """)

# Deposit to account line of code.....

elif int(customer_input) == 2:
    while True:
        account_no = int(input("Enter your account no to identify you: "))
        file = pd.read_fwf("account_list.txt", header=None)
        all_list = list(file.loc[:, 0])
        if account_no not in all_list:
            print("Account does not exist")
            print("Please try again.")
            exit()
        else:
            checking = data.check_account_name(account_no)
            print(f"Welcome back '{checking}'.")
            # print("Your can proceed with your transaction")
            break
    amount_input = int(input("How much do you want to Deposit: "))
    pin = int(input("Enter you security pin: "))
    data.deposit(account_no, pin, amount_input)
    data.commit()
    time.sleep(4)
    print(f"Your have successfully Deposited '{amount_input}'")

# Money Withdrawal for customer....

elif int(customer_input) == 3:
    amount_input = int(input("Enter the amount you want to Withdraw: "))
    account_no = int(input("Enter account no: "))
    pin = int(input("Enter you security pin: "))
    data.withdraw(account_no, pin, amount_input)
    data.commit()

# Transfer line of code....

elif int(customer_input) == 4:
    amount_input = int(input("Enter the amount you want to Transfer: "))

    account_no = int(input("Enter your account no: "))

    while True:
        to_account = int(input("Enter recipient no: "))
        file = pd.read_fwf("account_list.txt", header=None)
        all_list = list(file.loc[:, 0])
        if to_account not in all_list:
            print("Account does not exist")
            print("Your can only transfer to customer within this bank.")
            print("Please try again.")
            exit()
        else:
            print("Your can proceed with your transaction")
            break
    checking = data.check_account_name(to_account)
    print(f"The name of recipient is '{checking}'")

    pin = int(input("\nEnter you security pin: "))

    data.transfer(amount_input, account_no, pin, to_account)
    data.commit()
    time.sleep(3)
    print(f"You have successfully transfer '{amount_input}' to '{checking}'")
