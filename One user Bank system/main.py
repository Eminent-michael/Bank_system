"""
This is a Bank system program
        __Functions__
# -User can save money.
-User can transfer money
# -User can Check current balance
-User can recharge card from their account.
# -User can see all details about them with (all)
-User can invest their money.
"""


# //TODO: Create CSV file to collect single User:

class Account:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as file:
            self.balance = int(file.read())

    def deposit(self, amount=1000):
        if amount <= 0:
            print("You can not save amount less 0 or 0!")
        else:
            self.balance += amount

    def withdraw(self, amount=1000):
        if amount > self.balance:
            print("You can't request %d because your current \nbalance is %d." % (amount, self.balance))
        else:
            self.balance -= amount

    def commit(self):
        with open(self.filename, "w")as file:
            file.write(str(self.balance))


class Checking(Account):
    def __init__(self, filename, fee=10):
        super().__init__(
            filename
        )
        self.fee = fee

    def transfer(self, amount=100):
        if amount > self.balance:
            print("Insufficient balance as your balance is %d" % self.balance)
        elif amount <= 100:
            print("Your can not transfer amount less than 100")
        else:
            self.balance = self.balance - amount - self.fee


print("What would like us to do for you today?")
print("Enter '1' to Deposit Money.\nEnter '2' to Withdraw money.\nEnter '3' to Transfer.\nEnter '4' to Check Account Balance.")
customer_input = input("> ")

file_name = Account("customer.txt")
file_name2 = Checking("customer.txt")
if int(customer_input) == 1:
    amount_input = int(input("Enter the amount you want to Deposit: "))
    file_name.deposit(amount_input)
    file_name.commit()

elif int(customer_input) == 2:
    amount_input = int(input("Enter the amount you want to Withdraw: "))
    file_name.withdraw(amount_input)
    file_name.commit()

elif int(customer_input) == 3:
    amount_input = int(input("Enter the amount you want to Transfer: "))
    file_name2.transfer(amount_input)
    file_name2.commit()

elif int(customer_input) == 4:
    print(file_name.balance)

else:
    print("Invalid input!!!")

# print(file_name2.balance)
