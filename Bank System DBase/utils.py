import random
from backend import *


def account_num_list():
    account_details_list = []
    data = Account()
    account_no_list = data.accounts_email_list()
    for account_list in account_no_list:
        for acct_list in account_list:
            account_details_list.append(acct_list)
    return account_details_list


account_num_list()


def createAccount(data):
    name = input("Enter your name: ")
    while len(name) == 0:
        name = input("Enter your name: ")

    email = input("Enter your email: ")

    # This pick 6-digit number in random and check
    # if it exists in the account_list.txt it reruns the code (it's a while loop)
    # if it does then save the code in the account_list.txt file and print to save to database.
    while True:
        account_no = random.randint(100000, 999999)

        all_list = account_num_list()

        if account_no in all_list:
            time.sleep(2)
        else:
            break

    print(f"Please write down your account number '{account_no}', its only show once.")

    print('Your pin must be 4 digit and what you can easily remember')
    pin = input("Enter the 4 digit for your pin: ")

    while len(pin) > 4 or len(pin) < 4:
        print('Your pin must be 4 digit and what you can easily remember')
        pin = input("Enter the 4 digit for your pin: ")
    print(pin)
    data.create_account(name, email, account_no, pin)
    data.commit()
    print(f"""
        This is a one time message.
        Your name is {name}
        Your account number '{account_no}'
        Your pin is '{pin}'.
        Thank you for using our bank.
        """)

# DepositCash to user account


def depositCash(data1, data):
    account_no, pin = data.user_validation()

    checking = data.check_account_name(account_no)
    print(f"Welcome back '{checking}'.")

    amount_input = int(input("How much do you want to Deposit: "))
    pin = int(input("Enter you security pin: "))
    data1.deposit(account_no, pin, amount_input)
    data1.commit()
    time.sleep(3)
    print(f"Your have successfully Deposited '{amount_input}'")


def withdrawCash(data1, data):
    account_no, pin = data.user_validation()

    checking = data.check_account_name(account_no)
    print(f"Welcome back '{checking}'.")

    checking_balance = data.check_balance(account_no, pin)
    print(checking_balance)
    amount_input = int(input("Enter the amount you want to Withdraw: "))
    data1.withdraw(account_no, pin, amount_input)
    data1.commit()


def transferCash(data1):
    account_no, pin = data1.user_validation()

    amount_input = int(input("Enter the amount you want to Transfer: "))

    i = 0
    while i < 3:
        to_account = int(input("Enter recipient no: "))
        all_list = account_num_list()
        if to_account not in all_list:
            print("Account does not exist")
            print("Your can only transfer to customer within this bank.")
            print("If you made mistake please try again you have 2 trials.")
            i += 1
            if i == 3:
                print("We can't find this account number in out database.")
                exit()
        else:
            print("Your can proceed with your transaction")
            break
    checking = data1.check_account_name(to_account)
    print(f"The name of recipient is '{checking}'")

    pin = int(input("\nEnter you security pin: "))

    data1.transfer(amount_input, account_no, pin, to_account, checking)
    data1.commit()


def change_or_add_email(data1, update):
    account_no, pin = data1.user_validation()

    change_email = input("Enter your email: ")
    update.change_or_edit(account_no, pin, change_email)
    update.commit()
