import random
import time
from backend import *
from utils import *


dat = Account()
print(dat.all_info())
email_list = dat.accounts_email_list()
# print(email_list)
for emails in email_list:
    print(emails[0])

print("What would like us to do for you today?")
print(" ")
print("Enter '1' to Create Account.")
print("Enter '2' to Deposit Money.")
print("Enter '3' to Withdraw money.")
print("Enter '4' to Transfer.")
print("Enter '5' to Check Account Balance.")
print("Enter '6' to change or add email.")

customer_input = int(input("> "))
data = Account()
data1 = Account_update()
update = Update_info()


# Create account line of code......

if int(customer_input) == 1:
    createAccount(data)

# Deposit to account line of code.....

elif int(customer_input) == 2:
    depositCash(data1, data)

# Money Withdrawal for customer....

elif int(customer_input) == 3:
    withdrawCash(data1, data)

# Transfer line of code....

elif int(customer_input) == 4:
    transferCash(data1)


# Change of Email or add Email to the account
elif int(customer_input) == 6:
    change_or_add_email(update)
