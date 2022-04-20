"""
This is a Bank system program
        __Functions__
-User can create an account.
-User can deposit money.
-User can transfer money
-User can Check current balance
-User can recharge card from their account.
-User can see all details about them with (all)
-User can invest their money.
"""


# //TODO: Create CSV file to collect single User:

import sqlite3
import time


class Account:
    def __init__(self):
        self.connect = sqlite3.connect("Account.db")
        self.cur = self.connect.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, email TEXT, account_no INTEGER PRIMARY KEY, pin INTEGER, balance REAL)")

    def create_account(self, name, email="", account_no=0, pin=0, balance=0):
        self.cur.execute("INSERT INTO account VALUES(?,?,?,?,?)", (name, email, account_no, pin, balance))

    def user_validation(self):
        account_no = int(input("Enter your account number to identify you: "))
        pin = int(input("Enter your security pin: "))
        i = 1
        x = 0
        while i == 0 and x <= 3:
            valid_query = "SELECT name FROM account WHERE account_no = ? and pin = ?"
            self.cur.execute(valid_query, (account_no, pin))
            rows = self.cur.fetchone()
            print(rows)
            if rows is None:
                print("Account number or pin is no correct")
                print('Please try again\n')
                account_no = int(input("Enter your account no: "))
                pin = int(input("Enter your pin: "))

                x += 1
                i = 0
            else:
                print("Transaction processing....")
                break
        return account_no, pin

    def all_info(self):
        self.cur.execute("SELECT * FROM account")
        rows = self.cur.fetchall()
        return rows

    def accounts_email_list(self):
        self.cur.execute("SELECT account_no FROM account")
        rows = self.cur.fetchall()
        return rows

    def commit(self):
        self.connect.commit()
        self.connect.close()

    def check_balance(self, account_no, pin):
        self.cur.execute("SELECT balance FROM account WHERE account_no = ? and pin = ?", (account_no, pin))
        rows = self.cur.fetchone()[0]
        return f"Your current balance is '{rows}'"

    def check_account_name(self, recipient):
        self.cur.execute("SELECT name FROM account WHERE account_no = ?", (recipient,))
        rows = self.cur.fetchone()[0]
        return rows


class Account_update(Account):
    def __init__(self):
        super().__init__(

        )

    def deposit(self, account_no, pin, balance):
        self.cur.execute("UPDATE account SET balance=balance + ? WHERE account_no=? and pin=?", (balance, account_no, pin))

    def withdraw(self, account_no, pin, balance):
        self.cur.execute("SELECT balance FROM account WHERE account_no = ? and pin = ?", (account_no, pin))
        rows = self.cur.fetchone()[0]
        if balance > rows:
            print(f"Insufficient balance. Your current balance is '{rows}'")
        else:
            self.cur.execute("UPDATE account SET balance=balance - ? WHERE account_no=? and pin=?", (balance, account_no, pin))

    def transfer(self, amount, account_no, pin, recipient, checking):
        self.cur.execute("SELECT balance FROM account WHERE account_no = ? and pin = ?", (account_no, pin))
        rows = self.cur.fetchone()[0]
        if rows < amount:
            print("Insufficient balance as your balance is '%d'" % rows)
        elif amount < 100:
            print("You can not transfer amount less than 100")
        else:
            self.cur.execute("UPDATE account SET balance=balance - ? WHERE account_no=? and pin=?", (amount, account_no, pin))
            self.cur.execute("UPDATE account SET balance=balance + ? WHERE account_no=?", (amount, recipient))

            time.sleep(3)
            print(f"You have successfully transfer '%d' to '%s'" % (amount, checking))


class Update_info(Account):
    def __init__(self):
        super().__init__()

    def change_or_edit(self, account_no, pin, email):
        self.cur.execute("UPDATE account SET email = ? WHERE account_no = ? and pin = ?", (email, account_no, pin))
